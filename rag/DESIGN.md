# Verus RAG Design

## Goal

Build a practical retriever for Verus debugging:

- Input: user issue description + Rust/Verus code snippet + Verus error output
- Output: high-quality evidence from:
  - project code (`projects/**/*.rs`)
  - tutorial docs (`tutorial/**/*.md|txt|rst`)
  - PDF knowledge (page-level chunks)

## Indexing Pipeline

1. **Source discovery**
   - Project Rust code from `projects/`
   - Tutorial text docs from `tutorial/`
   - PDF files from configurable roots (`--pdf-roots`, default `.`)
2. **Chunking**
   - Rust code: line windows (80 lines, overlap 20)
   - Docs: char windows (1400 chars, overlap 200)
   - PDF: per-page extraction, then char windows (1500 chars, overlap 220)
3. **Metadata**
   - `source_group`, `path`, `line_start`, `line_end`, `page`
   - `title`, `tags` (requires/ensures/invariant/etc), token length
4. **Storage**
   - `chunks.jsonl`
   - `meta.json`

## Retrieval Pipeline

### Stage 1 – Query Construction (code_analyzer + error_cleaner)

**Code analysis** (`rag/code_analyzer.py`):
- Extracts tokens specifically from `ensures`/`requires`/`invariant` blocks with **3.5× weight**
  (spec clauses are far more semantically distinctive than generic code)
- Detects **proof patterns** (min_element, max_element, sum_prefix, linear_search, reverse,
  rotate, append, abs, unique, tangent, arithmetic_cast, …) and injects them as bonus query terms
- Extracts key identifiers repeated ≥2 times (likely meaningful function/type names)
- Generates a `spec_summary` string for the semantic query: `ensures: …\nrequires: …\nproof_patterns: …`

**Error analysis** (`rag/error_cleaner.py`):
- Strips noisy lines (file paths, line numbers, generic notes)
- Detects **error categories** from both Verus phrases and Rust `E0xxx` codes:
  `postcondition`, `invariant`, `precondition`, `overflow`, `type_mismatch`,
  `assertion`, `missing_item`, `mode_error`, `old_ref`, `trigger`
- Expands each category into domain-specific hint terms

### Stage 2 – BM25 Lexical Ranking

- Weighted query Counter: `error` (1.6×), `spec_clause_tokens` (3.5×), `query` (1.0×)
- Standard Okapi BM25 with k₁=1.5, b=0.75
- **Hard exclusion** of off-topic path fragments (`getting_started`, `changelog`, etc.)
  before scoring (not penalized – completely removed)

### Stage 3 – Semantic Re-ranking (`rag/semantic.py`)

The semantic query uses `spec_summary` (ensures/requires/invariant text) instead of raw code,
giving the embedder a cleaner structural signal.

**Projection backend** (offline, no model download needed):
- Base tokens: Verus spec keywords get 2× weight
- Token **bigrams**: spec-adjacent pairs get 2.5× weight (captures "ensures forall", etc.)
- Spec clause tokens: extracted and hashed with **4× weight**
- Spec bigrams: 3× weight
- Character trigrams of symbolic patterns (0.2×)
- **Structural fingerprint**: counts of forall/exists/invariant/ensures/requires encoded as
  explicit features (3× weight) – ensures that two chunks with different spec shapes have
  different embeddings even if surface tokens overlap

**SentenceTransformer backend**: used when a locally cached model is found (`local_files_only=True`).

### Stage 4 – RRF Fusion + Group Boosting

- Reciprocal Rank Fusion merges lexical and semantic rankings (k=60)
- Source priors: pdf=0.28 > project=0.16 > tutorial=0.14
- Verus keyword overlap boost (+0.05/kw, capped at 0.25)
- Jaccard token overlap with query (×0.6)
- Path-aware adjustments: up-rank pages matching error-category topics (+0.10/kw),
  down-rank known noise tutorial paths (−0.30)

### Stage 5 – Diversification

- Near-duplicate suppression (same file ±8 lines, or Jaccard snippet > 0.87)
- Group minimum coverage (`min_project`, `min_tutorial`, `min_pdf`)
- **Per-repo limit** (default 2) for project source group – prevents a single large
  project from dominating all project slots
- Two-phase selection: satisfy group minimums first, then fill by global rank

### Stage 6 – LLM Packaging

- Structured JSON: `results`, `grouped`, `error_categories`, `proof_patterns`,
  `cleaned_error_preview`, `retrieval_debug` (backend, candidate counts, spec_summary)
- `prompt_pack`: compact plain-text block for direct LLM context injection
- Optional `--prompt-out` file

## Why PDF Is First-Class

- PDF often contains conceptual explanations missing from code comments.
- The retriever enforces PDF quota (`--min-pdf`) when PDF exists.
- Output uses page-aware citation (`file.pdf#page-N`) for precise follow-up.

## Quality Assessment Results (16 examples, April 2026)

After iterative improvements, batch evaluation on 16 `examples/*.rs` files shows:

| Metric | Value |
|--------|-------|
| Examples scored HIGH | 16/16 |
| PDF hits relevant | ~100% |
| Tutorial hits relevant | ~75% |
| Noise documents in top-8 | 0% |

Key error categories handled well:
- `postcondition + invariant` → `while.md`, PDF loop chapters, project loop proofs
- `overflow` → `integers.md`, `CheckedU128.md`, PDF integer chapters
- `type_mismatch (E0308)` → `reference-as.md`, `integers.md`, `exec_spec.md`
- `missing_item (E0599)` → `vstd_api` docs, vec/seq library chunks
- `old_ref` → `mut-ref.md`, `requires-ensures.md`

## Future Extensions

- Add vector embeddings (CodeBERT / UniXcoder) for better project code semantic matching.
- Add module-aware code chunking (function-level boundary detection).
- Add online serving endpoint (`FastAPI`) and persistent cache.
- Add benchmark set from historical Verus errors for regression testing.
- Cross-reference project examples: link chunks from the same function/module for richer context.
