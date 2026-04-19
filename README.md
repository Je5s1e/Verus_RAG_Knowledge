# Verus RAG Knowledge Base

A specialized knowledge base and local retrieval-augmented generation (RAG) system for Verus formal verification. It aggregates high-value external knowledge — official tutorial documentation, verified codebases from open-source repositories, and PDF references — and provides LLMs with precise, structured context for Verus proof debugging and specification generation.

---

## Knowledge Sources

### Core Tooling & Standard Library

| Source | Description | Link |
| --- | --- | --- |
| **Verus Core** | The primary repository for the Verus verifier and the `vstd` source code. | [verus-lang/verus](https://github.com/verus-lang/verus) |
| **VSTD API** | The official API reference for the Verus Standard Library (essential for `requires`/`ensures` contracts). | [vstd Documentation](https://verus-lang.github.io/verus/verusdoc/vstd/) |

### Documentation & Theoretical Guides

| Source | Knowledge Type | Link |
| --- | --- | --- |
| **Verus Guide** | Comprehensive tutorial covering syntax, proof techniques, and the `verus!` macro. | [Verus Guide & Reference](https://verus-lang.github.io/verus/guide/) |
| **Transition Systems** | Specialized documentation for verifying state machines and asynchronous logic. | [State Machines Guide](https://verus-lang.github.io/verus/state_machines/) |

### Verified System Projects (Golden Examples)

Production-grade verified projects providing complex, real-world proof patterns for the RAG system.

| Project | Domain | Link |
| --- | --- | --- |
| **VeriSMo** | A verified security module for confidential virtual machines. | [microsoft/verismo](https://github.com/microsoft/verismo) |
| **Anvil** | A framework for verifying Kubernetes controllers. | [anvil-verifier/anvil](https://github.com/anvil-verifier/anvil) |
| **Vest** | A high-performance verified binary parser and serializer framework. | [secure-foundations/vest](https://github.com/secure-foundations/vest) |
| **IronKV** | A formally verified, sharded key-value store. | [verus-lang/verified-ironkv](https://github.com/verus-lang/verified-ironkv) |

---

## RAG System Architecture

The retrieval pipeline accepts three inputs — a natural language description, a Rust/Verus code snippet, and a Verus error message — and returns ranked, deduplicated evidence from three source groups: `project` (verified code), `tutorial` (docs), and `pdf` (slides/papers).

### Pipeline Overview

```
Input (query + code + error)
        │
        ▼
┌─────────────────────────────┐
│  Stage 1: Query Construction │  code_analyzer + error_cleaner
│  - Extract spec tokens       │  ensures/requires/invariant → 3.5× weight
│  - Detect proof patterns     │  e.g. min_element, sum_prefix, linear_search
│  - Clean error message       │  strip paths/stack noise, expand error hints
└──────────────┬──────────────┘
               │
       ┌───────┴───────┐
       ▼               ▼
┌─────────────┐  ┌──────────────────┐
│  Stage 2    │  │    Stage 3        │
│  BM25       │  │  Semantic Rerank  │
│  Lexical    │  │  (spec_summary    │
│  Ranking    │  │   as query)       │
└──────┬──────┘  └────────┬─────────┘
       └────────┬──────────┘
                ▼
┌───────────────────────────────┐
│  Stage 4: RRF Fusion          │  Reciprocal Rank Fusion (k=60)
│  + source priors + boosting   │  pdf > project > tutorial
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│  Stage 5: Diversification     │  near-duplicate suppression
│  + group minimum coverage     │  per-repo limit, group quotas
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│  Stage 6: LLM Packaging       │  prompt_pack + optional --prompt-out
└───────────────────────────────┘
```

### Key Design Choices

- **Spec-weighted BM25**: tokens from `ensures`/`requires`/`invariant` blocks are boosted 3.5× over regular code tokens, since spec clauses are far more semantically distinctive.
- **Semantic backend**: uses a locally cached SentenceTransformer model when available; falls back to a projection-based embedding (offline-friendly, no model download required).
- **Error cleaning**: strips file paths, line numbers, and stack noise from Verus error output; detects error categories (`postcondition`, `invariant`, `overflow`, `type_mismatch`, etc.) and expands them into domain-specific hint terms.
- **PDF as first-class source**: PDF pages are chunked and windowed with overlap, and a minimum PDF quota is enforced in the final results.
- **Diversification**: near-duplicate suppression (same file ±8 lines, Jaccard > 0.87), per-repo project cap (default 2), and two-phase group-minimum selection.

For the full retrieval architecture, see [`rag/DESIGN.md`](rag/DESIGN.md).

---

## Setup

**Install dependencies** (Python 3.9+):

```bash
pip install pypdf>=5.0.0
# Optional: for SentenceTransformer semantic backend
pip install sentence-transformers
```

**Repository layout:**

```
Verus_RAG_Knowledge/
├── projects/          # Verified Verus projects (golden examples)
│   ├── anvil-main/
│   ├── verified-ironkv/
│   ├── verismo/
│   └── vest-main/
├── tutorial/          # Docs, markdown guides, PDF references
│   ├── verus/
│   ├── vstd_api_md/
│   ├── Verus_Tutorial_and_Reference.pdf
│   └── Verus_Transition_Systems.pdf
├── rag/               # Retrieval pipeline source code
├── rag_cli.py         # CLI entry point
└── .rag_index/        # Built index (generated, not committed)
```

---

## Usage

### 1. Build the Index

```bash
python rag_cli.py build \
  --repo-root . \
  --index-dir .rag_index \
  --pdf-roots ".,tutorial,docs" \
  --force-tutorial-pdf
```

| Flag | Description |
| --- | --- |
| `--repo-root` | Root of the repository to index (default: `.`) |
| `--index-dir` | Output directory for the built index |
| `--pdf-roots` | Comma-separated directories to scan for PDF files |
| `--force-tutorial-pdf` | Always include `tutorial/` in PDF discovery |

The index is stored as `chunks.jsonl` and `meta.json` under `--index-dir`. Re-run with `--force` to rebuild from scratch.

### 2. Query the Index

```bash
python rag_cli.py query \
  --index-dir .rag_index \
  --query-text "loop invariant fails for map update" \
  --code-file /path/to/your_snippet.rs \
  --error-file /path/to/verus_error.txt \
  --top-k 12 \
  --per-group-k 6 \
  --min-project 2 \
  --min-tutorial 2 \
  --min-pdf 2 \
  --semantic-backend auto \
  --semantic-candidate-k 1200 \
  --prompt-out /tmp/verus_rag_context.txt
```

| Flag | Description |
| --- | --- |
| `--query-text` | Natural language description of the problem |
| `--code-file` | Path to the Rust/Verus source file |
| `--error-file` | Path to the Verus error output |
| `--top-k` | Total number of results to return |
| `--per-group-k` | Max results per source group |
| `--min-project/tutorial/pdf` | Minimum results from each source group |
| `--semantic-backend` | `auto` (prefer local model), `projection` (offline), or `none` |
| `--prompt-out` | Save the LLM-ready context block to a file |

The output includes a `prompt_pack` field — a compact plain-text block ready for direct LLM context injection. If `--prompt-out` is specified, this block is also written to a file.

### 3. Programmatic Usage

```python
from rag.retriever import Retriever

retriever = Retriever(index_dir=".rag_index")
results = retriever.query(
    query_text="postcondition fails after loop",
    code="fn foo(v: &Vec<u64>) ...",
    error="postcondition not satisfied\n  ensures result == ...",
    top_k=10,
)
print(results["prompt_pack"])
```

---

## Retrieval Quality

Batch evaluation on 16 representative Verus examples (April 2026):

| Metric | Value |
| --- | --- |
| Examples scored HIGH | 16 / 16 |
| PDF hits relevant | ~100% |
| Tutorial hits relevant | ~75% |
| Noise documents in top-8 | 0% |

Key error categories and their typical retrieval targets:

| Error Category | Retrieved Sources |
| --- | --- |
| `postcondition + invariant` | `while.md`, PDF loop chapters, project loop proofs |
| `overflow` | `integers.md`, `CheckedU128.md`, PDF integer chapters |
| `type_mismatch (E0308)` | `reference-as.md`, `integers.md`, `exec_spec.md` |
| `missing_item (E0599)` | `vstd_api` docs, vec/seq library chunks |
| `old_ref` | `mut-ref.md`, `requires-ensures.md` |
