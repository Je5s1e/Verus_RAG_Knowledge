"""Index builder for Verus RAG retrieval."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

from .tokenize import token_counts

CODE_EXTENSIONS = {".rs"}
DOC_EXTENSIONS = {".md", ".txt", ".rst"}
PDF_EXTENSIONS = {".pdf"}
IGNORE_DIR_NAMES = {".git", ".rag_index", "__pycache__", ".venv", "node_modules"}

CODE_LINE_CHUNK = 80
CODE_LINE_OVERLAP = 20
DOC_CHAR_CHUNK = 1400
DOC_CHAR_OVERLAP = 200
PDF_CHAR_CHUNK = 1500
PDF_CHAR_OVERLAP = 220


@dataclass
class Chunk:
    id: str
    path: str
    source_type: str
    source_group: str
    lang: str
    text: str
    line_start: int
    line_end: int
    page: int
    title: str
    tags: list[str]
    token_len: int
    text_hash: str


def _iter_files(
    root: Path,
    include_pdfs: bool,
    pdf_roots: list[str] | None,
) -> Iterable[tuple[Path, str, str]]:
    projects_dir = root / "projects"
    tutorial_dir = root / "tutorial"

    if projects_dir.exists():
        for path in _walk_files(projects_dir):
            if path.suffix.lower() in CODE_EXTENSIONS:
                yield path, "code", "project"

    if tutorial_dir.exists():
        for path in _walk_files(tutorial_dir):
            suffix = path.suffix.lower()
            if suffix in DOC_EXTENSIONS:
                yield path, "doc", "tutorial"

    if include_pdfs:
        roots = [root]
        if pdf_roots:
            roots = [root / rel for rel in pdf_roots]
        seen: set[Path] = set()
        for pdf_root in roots:
            if not pdf_root.exists():
                continue
            for path in _walk_files(pdf_root):
                if path.suffix.lower() not in PDF_EXTENSIONS:
                    continue
                path = path.resolve()
                if path in seen:
                    continue
                seen.add(path)
                yield path, "doc", "pdf"


def _walk_files(base: Path) -> Iterable[Path]:
    """Iterate files with explicit ignore-dir pruning.

    Using os.walk here is more predictable than rglob for very large trees.
    """
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIR_NAMES]
        for name in filenames:
            path = Path(dirpath) / name
            if any(part in IGNORE_DIR_NAMES for part in path.parts):
                continue
            yield path


def _chunk_code_lines(lines: list[str]) -> list[tuple[int, int, str]]:
    chunks: list[tuple[int, int, str]] = []
    i = 0
    total = len(lines)
    while i < total:
        end = min(total, i + CODE_LINE_CHUNK)
        block = "".join(lines[i:end]).strip()
        if block:
            chunks.append((i + 1, end, block))
        if end == total:
            break
        i += CODE_LINE_CHUNK - CODE_LINE_OVERLAP
    return chunks


def _chunk_doc_text(
    text: str, chunk_size: int = DOC_CHAR_CHUNK, overlap: int = DOC_CHAR_OVERLAP
) -> list[tuple[int, int, str]]:
    chunks: list[tuple[int, int, str]] = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = min(text_len, start + chunk_size)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append((1, 1, chunk))
        if end == text_len:
            break
        start += chunk_size - overlap
    return chunks


def _read_pdf_pages(path: Path) -> tuple[list[tuple[int, str]], str]:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return [], "pypdf_not_installed"

    try:
        reader = PdfReader(str(path))
        pages: list[tuple[int, str]] = []
        for idx, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            text = _clean_doc_text(text)
            if text:
                pages.append((idx + 1, text))
        return pages, ""
    except Exception as exc:
        return [], f"parse_error:{exc.__class__.__name__}"


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def _clean_doc_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def _infer_tags(text: str) -> list[str]:
    low = text.lower()
    keys = (
        "requires",
        "ensures",
        "invariant",
        "decreases",
        "forall",
        "exists",
        "lemma",
        "proof",
        "trigger",
        "spec",
        "ghost",
        "loop",
    )
    return [k for k in keys if k in low]


def _guess_title(path: Path, text: str) -> str:
    if path.suffix.lower() == ".md":
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("#"):
                return line.lstrip("#").strip()[:120]
    return path.stem


def _hash_text(text: str) -> str:
    compact = " ".join(text.split())
    return hashlib.md5(compact.encode("utf-8")).hexdigest()  # noqa: S324


def build_index(
    repo_root: str | Path,
    output_dir: str | Path = ".rag_index",
    include_pdfs: bool = True,
    pdf_roots: list[str] | None = None,
) -> dict:
    root = Path(repo_root).resolve()
    out = Path(output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)

    chunks: list[Chunk] = []
    idx = 0
    discovered_counts = {"project_files": 0, "tutorial_files": 0, "pdf_files": 0}
    discovered_pdf_files: list[str] = []
    pdf_parse_failures: list[dict[str, str]] = []
    parsed_pdf_file_set: set[str] = set()
    for file_path, source_type, source_group in _iter_files(root, include_pdfs, pdf_roots):
        if source_group == "project":
            discovered_counts["project_files"] += 1
        elif source_group == "tutorial":
            discovered_counts["tutorial_files"] += 1
        elif source_group == "pdf":
            discovered_counts["pdf_files"] += 1
            discovered_pdf_files.append(str(file_path.relative_to(root)))

        if source_group == "pdf":
            pages, err = _read_pdf_pages(file_path)
            if not pages:
                pdf_parse_failures.append(
                    {
                        "path": str(file_path.relative_to(root)),
                        "reason": err or "empty_pdf_or_no_extractable_text",
                    }
                )
                continue
            rel = str(file_path.relative_to(root))
            parsed_pdf_file_set.add(rel)
            for page_no, page_text in pages:
                chunked = _chunk_doc_text(
                    page_text, chunk_size=PDF_CHAR_CHUNK, overlap=PDF_CHAR_OVERLAP
                )
                for line_start, line_end, text in chunked:
                    tks = token_counts(text)
                    chunks.append(
                        Chunk(
                            id=f"chunk-{idx}",
                            path=rel,
                            source_type=source_type,
                            source_group=source_group,
                            lang="pdf",
                            text=text,
                            line_start=line_start,
                            line_end=line_end,
                            page=page_no,
                            title=file_path.stem,
                            tags=_infer_tags(text),
                            token_len=sum(tks.values()),
                            text_hash=_hash_text(text),
                        )
                    )
                    idx += 1
            continue
        elif source_type == "code":
            raw = _read_text(file_path)
            lines = raw.splitlines(keepends=True)
            chunked = _chunk_code_lines(lines)
            lang = "rust"
        else:
            raw = _read_text(file_path)
            chunked = _chunk_doc_text(_clean_doc_text(raw))
            lang = "markdown"

        rel = str(file_path.relative_to(root))
        title = _guess_title(file_path, raw)
        for line_start, line_end, text in chunked:
            tks = token_counts(text)
            chunks.append(
                Chunk(
                    id=f"chunk-{idx}",
                    path=rel,
                    source_type=source_type,
                    source_group=source_group,
                    lang=lang,
                    text=text,
                    line_start=line_start,
                    line_end=line_end,
                    page=0,
                    title=title,
                    tags=_infer_tags(text),
                    token_len=sum(tks.values()),
                    text_hash=_hash_text(text),
                )
            )
            idx += 1

    chunks_path = out / "chunks.jsonl"
    with chunks_path.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(asdict(c), ensure_ascii=False) + "\n")

    # Persist minimal stats for quick loading.
    doc_lens = [c.token_len for c in chunks]
    avg_len = (sum(doc_lens) / len(doc_lens)) if doc_lens else 0.0
    chunk_by_group = {
        "project": sum(1 for c in chunks if c.source_group == "project"),
        "tutorial": sum(1 for c in chunks if c.source_group == "tutorial"),
        "pdf": sum(1 for c in chunks if c.source_group == "pdf"),
    }
    files_by_group = {
        "project": len({c.path for c in chunks if c.source_group == "project"}),
        "tutorial": len({c.path for c in chunks if c.source_group == "tutorial"}),
        "pdf": len({c.path for c in chunks if c.source_group == "pdf"}),
    }
    metadata = {
        "repo_root": str(root),
        "chunk_count": len(chunks),
        "avg_token_len": avg_len,
        "sources": {
            "project_code_chunks": chunk_by_group["project"],
            "tutorial_doc_chunks": chunk_by_group["tutorial"],
            "pdf_doc_chunks": chunk_by_group["pdf"],
            "project_files": files_by_group["project"],
            "tutorial_files": files_by_group["tutorial"],
            "pdf_files": files_by_group["pdf"],
            "discovered_project_files": discovered_counts["project_files"],
            "discovered_tutorial_files": discovered_counts["tutorial_files"],
            "discovered_pdf_files": discovered_counts["pdf_files"],
        },
        "pdf_indexing": {
            "include_pdfs": include_pdfs,
            "pdf_roots": pdf_roots or ["."],
            "pdf_chunk_size_chars": PDF_CHAR_CHUNK,
            "pdf_chunk_overlap_chars": PDF_CHAR_OVERLAP,
            "parsed_pdf_files": len(parsed_pdf_file_set),
            "failed_pdf_files": len(pdf_parse_failures),
            "discovered_pdf_paths": discovered_pdf_files[:50],
            "failed_pdf_examples": pdf_parse_failures[:20],
        },
    }
    (out / "meta.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if include_pdfs and discovered_counts["pdf_files"] > 0 and len(parsed_pdf_file_set) == 0:
        print(
            "[WARN] Found PDF files but parsed 0 successfully. "
            "Check pypdf installation and PDF extractability. "
            "See .rag_index/meta.json -> pdf_indexing.failed_pdf_examples",
            file=sys.stderr,
        )
    return metadata
