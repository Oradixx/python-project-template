"""Business logic lives here: pure functions, easy to test.

This example is deliberately tiny — delete it once you add your own code.
"""

from collections import Counter


def word_count(text: str, *, top: int | None = None) -> list[tuple[str, int]]:
    """Count case-insensitive word occurrences, most frequent first.

    Args:
        text: Any string.
        top: If given, keep only the ``top`` most frequent words.

    Returns:
        A list of ``(word, count)`` pairs sorted by decreasing count.
    """
    if top is not None and top < 1:
        raise ValueError("top must be a positive integer")
    words = (w.strip(".,;:!?\"'()[]").lower() for w in text.split())
    counts = Counter(w for w in words if w)
    return counts.most_common(top)
