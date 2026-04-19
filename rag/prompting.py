"""Utilities to convert retrieval output into LLM-ready prompt context."""

from __future__ import annotations


def render_prompt_context(result: dict, max_items: int = 10) -> str:
    items = (result or {}).get("results", [])[:max_items]
    blocks: list[str] = []
    for idx, item in enumerate(items, 1):
        path = item.get("path", "")
        line_start = item.get("line_start", 1)
        line_end = item.get("line_end", 1)
        page = item.get("page", 0)
        location = f"{path}:{line_start}-{line_end}"
        if page:
            location = f"{path}#page-{page}"
        group = item.get("source_group", "unknown")
        tags = ", ".join(item.get("tags", [])[:6]) or "none"
        snippet = item.get("snippet", "")
        blocks.append(
            (
                f"[Context {idx}] group={group} loc={location} tags={tags}\n"
                f"{snippet}"
            )
        )

    guidance = (
        "You are helping debug Verus code. Prefer evidence from project snippets first; "
        "when proof obligations are unclear, reconcile with tutorial/pdf references."
    )
    return f"{guidance}\n\n" + "\n\n".join(blocks)
