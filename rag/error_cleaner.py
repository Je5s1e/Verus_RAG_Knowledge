"""Normalize Verus error outputs into retrieval-friendly signals."""

from __future__ import annotations

import re

NOISE_PATTERNS = [
    r"--> .*?:\d+:\d+",
    r"^\s*\|\s*$",
    r"^\s*\d+\s+\|.*$",
    r"^\s*= note:.*$",
    r"^\s*note: .*not all errors may have been reported.*$",
    r"^\s*For more information.*$",
    r"^\s*help:.*$",
    r"^\s*\^+\s*$",
]

KEEP_PREFIXES = (
    "error:",
    "error[",
    "failed",
    "precondition",
    "postcondition",
    "invariant",
    "assertion",
)

# ── Error category term expansions ───────────────────────────────────────────

ERROR_CATEGORY_TERMS: dict[str, list[str]] = {
    "precondition": ["requires", "precondition", "index", "bound", "len", "call"],
    "postcondition": ["ensures", "postcondition", "return", "result", "spec", "fn"],
    "invariant": ["invariant", "loop", "while", "decreases", "inductive", "state"],
    "overflow": ["overflow", "underflow", "arithmetic", "int", "nat", "bound", "cast", "as", "u64", "i32", "u128"],
    "type_mismatch": ["type", "cast", "as", "int", "usize", "i32", "u64", "mode", "exec", "spec", "ghost", "view"],
    "trigger": ["trigger", "forall", "exists", "quantifier", "choose"],
    "assertion": ["assert", "proof", "lemma", "calc", "by", "assert_by"],
    "missing_item": ["vstd", "seq", "vec", "prelude", "method", "function", "import", "use"],
    "mode_error": ["exec", "spec", "proof", "ghost", "tracked", "mode", "view"],
    "old_ref": ["old", "mut", "mutable", "reference", "borrow", "requires", "ensures"],
}

# ── Rust compiler error code mapping ─────────────────────────────────────────

# E-code -> category
_ECODE_TO_CATEGORY: dict[str, str] = {
    "E0308": "type_mismatch",
    "E0282": "type_mismatch",
    "E0277": "type_mismatch",
    "E0599": "missing_item",
    "E0425": "missing_item",
    "E0412": "missing_item",
    "E0433": "missing_item",
    "E0107": "type_mismatch",
}

# ── Verus-specific error phrase mapping ──────────────────────────────────────

_VERUS_PHRASE_TO_CATEGORY: dict[str, str] = {
    "precondition not satisfied": "precondition",
    "postcondition not satisfied": "postcondition",
    "invariant not satisfied": "invariant",
    "invariant not satisfied before loop": "invariant",
    "invariant not satisfied at end of loop body": "invariant",
    "possible arithmetic underflow/overflow": "overflow",
    "possible arithmetic overflow": "overflow",
    "possible arithmetic underflow": "overflow",
    "assertion failed": "assertion",
    "assertion not satisfied": "assertion",
    "assert_by failed": "assertion",
    "trigger may be insufficient": "trigger",
    "recommendation not met": "precondition",
    "failed to simplify": "assertion",
    "could not prove": "assertion",
    "cannot prove": "assertion",
    "mismatched types": "type_mismatch",
    "expected `int`, found `usize`": "type_mismatch",
    "expected `usize`, found `int`": "type_mismatch",
    "expected `i32`": "type_mismatch",
    "expected `u64`": "type_mismatch",
    "type annotations needed": "type_mismatch",
    "no associated item": "missing_item",
    "not found in this scope": "missing_item",
    "expected mutable reference": "old_ref",
    "arguments to this function are incorrect": "type_mismatch",
    "mode error": "mode_error",
    "cannot use spec": "mode_error",
    "exec code cannot call spec": "mode_error",
    "cannot call spec fn": "mode_error",
}


def _strip_noise_lines(lines: list[str]) -> list[str]:
    kept: list[str] = []
    for line in lines:
        s = line.rstrip()
        if not s:
            continue
        if any(re.match(pat, s) for pat in NOISE_PATTERNS):
            continue
        kept.append(s)
    return kept


def detect_error_categories(text: str) -> list[str]:
    """Return a deduplicated list of Verus/Rust error categories found in text."""
    low = text.lower()
    categories: list[str] = []
    seen: set[str] = set()

    def _add(cat: str) -> None:
        if cat not in seen:
            seen.add(cat)
            categories.append(cat)

    # Verus-specific phrases (most informative)
    for phrase, cat in _VERUS_PHRASE_TO_CATEGORY.items():
        if phrase in low:
            _add(cat)

    # Rust error codes  e.g. error[E0308]
    for code, cat in _ECODE_TO_CATEGORY.items():
        if code.lower() in low:
            _add(cat)

    return categories


def clean_error_text(error_text: str, max_lines: int = 80) -> str:
    """Strip noise lines and return a focused error summary."""
    lines = error_text.splitlines()
    lines = _strip_noise_lines(lines)

    focused: list[str] = []
    for line in lines:
        ll = line.lower().strip()
        # Keep error headlines, Verus-specific phrases, failed messages
        if (
            ll.startswith(KEEP_PREFIXES)
            or "not satisfied" in ll
            or "failed" in ll
            or "overflow" in ll
            or "underflow" in ll
            or "mismatched" in ll
            or "type annotation" in ll
            or "no associated item" in ll
            or "not found in this scope" in ll
            or re.match(r"error\[e\d+\]", ll)
        ):
            focused.append(line)

    if not focused:
        focused = lines
    focused = focused[:max_lines]
    return "\n".join(focused).strip()


def expand_terms_from_categories(categories: list[str]) -> list[str]:
    """Return a deduplicated list of retrieval hint terms for given categories."""
    terms: list[str] = []
    for cat in categories:
        terms.extend(ERROR_CATEGORY_TERMS.get(cat, []))
    return sorted(set(terms))
