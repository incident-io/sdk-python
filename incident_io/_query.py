"""Query-string helpers added by scripts/fix_generated.py."""

from __future__ import annotations

from typing import Any


def flatten_deep_object(name: str, value: Any) -> dict[str, Any]:
    """Flatten an object-valued query parameter into bracketed keys.

    The API's filters are objects keyed by operator, and some nest a second
    level keyed by field ID:

        flatten_deep_object("created_at", {"gte": ["2024-05-01"]})
        -> {"created_at[gte]": ["2024-05-01"]}

        flatten_deep_object("custom_field", {"01ABC": {"one_of": ["x"]}})
        -> {"custom_field[01ABC][one_of]": ["x"]}

    See scripts/fix_generated.py for why the generated client needs this.
    """
    flattened: dict[str, Any] = {}

    for key, inner in value.items():
        bracketed = f"{name}[{key}]"
        if isinstance(inner, dict):
            flattened.update(flatten_deep_object(bracketed, inner))
        else:
            flattened[bracketed] = inner

    return flattened
