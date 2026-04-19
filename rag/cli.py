"""CLI for building and querying Verus RAG index."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .index_builder import build_index
from .prompting import render_prompt_context
from .retriever import query_index


def _load_optional_text(text: str | None, text_file: str | None) -> str:
    if text and text_file:
        raise ValueError("请二选一：直接传文本或文件路径，不能同时传。")
    if text:
        return text
    if text_file:
        return Path(text_file).read_text(encoding="utf-8")
    return ""


def cmd_build(args: argparse.Namespace) -> int:
    pdf_roots = [p.strip() for p in args.pdf_roots.split(",") if p.strip()]
    if args.force_tutorial_pdf and "tutorial" not in pdf_roots:
        pdf_roots.append("tutorial")
    meta = build_index(
        repo_root=args.repo_root,
        output_dir=args.index_dir,
        include_pdfs=not args.no_pdf,
        pdf_roots=pdf_roots if pdf_roots else None,
    )
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


def cmd_query(args: argparse.Namespace) -> int:
    query_text = _load_optional_text(args.query_text, args.query_file)
    code_text = _load_optional_text(args.code_text, args.code_file)
    error_text = _load_optional_text(args.error_text, args.error_file)

    result = query_index(
        index_dir=args.index_dir,
        query_text=query_text,
        code_text=code_text,
        error_text=error_text,
        top_k=args.top_k,
        per_group_k=args.per_group_k,
        min_project=args.min_project,
        min_tutorial=args.min_tutorial,
        min_pdf=args.min_pdf,
        semantic_backend=args.semantic_backend,
        semantic_model=args.semantic_model,
        semantic_proj_dim=args.semantic_proj_dim,
        semantic_candidate_k=args.semantic_candidate_k,
        lexical_rrf_weight=args.lexical_rrf_weight,
        semantic_rrf_weight=args.semantic_rrf_weight,
    )
    if args.prompt_out:
        context_text = render_prompt_context(result, max_items=args.prompt_items)
        Path(args.prompt_out).write_text(context_text, encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rag_cli",
        description="Verus RAG: 从 projects/tutorial/pdf 检索相关内容。",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build", help="构建索引")
    p_build.add_argument("--repo-root", default=".", help="知识库根目录")
    p_build.add_argument("--index-dir", default=".rag_index", help="索引输出目录")
    p_build.add_argument("--no-pdf", action="store_true", help="不处理 PDF")
    p_build.add_argument(
        "--pdf-roots",
        default=".",
        help="PDF 扫描根目录（相对 repo-root，逗号分隔），默认扫描整个仓库。",
    )
    p_build.add_argument(
        "--force-tutorial-pdf",
        action="store_true",
        help="强制把 tutorial 目录加入 PDF 扫描根目录。",
    )
    p_build.set_defaults(func=cmd_build)

    p_query = sub.add_parser("query", help="执行检索")
    p_query.add_argument("--index-dir", default=".rag_index", help="索引目录")
    p_query.add_argument("--query-text", default=None, help="问题文本")
    p_query.add_argument("--query-file", default=None, help="问题文本文件")
    p_query.add_argument("--code-text", default=None, help="代码片段文本")
    p_query.add_argument("--code-file", default=None, help="代码片段文件")
    p_query.add_argument("--error-text", default=None, help="报错文本")
    p_query.add_argument("--error-file", default=None, help="报错文本文件")
    p_query.add_argument("--top-k", type=int, default=12, help="总体返回条数")
    p_query.add_argument("--per-group-k", type=int, default=6, help="每组最多返回条数")
    p_query.add_argument("--min-project", type=int, default=2, help="最终结果中最少 project 条数")
    p_query.add_argument("--min-tutorial", type=int, default=2, help="最终结果中最少 tutorial 条数")
    p_query.add_argument("--min-pdf", type=int, default=2, help="最终结果中最少 pdf 条数")
    p_query.add_argument(
        "--semantic-backend",
        default="auto",
        choices=["auto", "sentence-transformer", "projection"],
        help="语义检索后端：auto 优先 sentence-transformer，否则退化到 projection。",
    )
    p_query.add_argument(
        "--semantic-model",
        default="all-MiniLM-L6-v2",
        help="sentence-transformer 模型名（在对应后端可用时生效）。",
    )
    p_query.add_argument("--semantic-proj-dim", type=int, default=256, help="projection 向量维度")
    p_query.add_argument("--semantic-candidate-k", type=int, default=1200, help="语义重排候选数")
    p_query.add_argument("--lexical-rrf-weight", type=float, default=1.0, help="RRF 中 lexical 权重")
    p_query.add_argument("--semantic-rrf-weight", type=float, default=0.9, help="RRF 中 semantic 权重")
    p_query.add_argument("--prompt-out", default=None, help="可选：输出 LLM 上下文文本文件路径")
    p_query.add_argument("--prompt-items", type=int, default=10, help="写入 LLM 上下文的最大条数")
    p_query.set_defaults(func=cmd_query)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)
