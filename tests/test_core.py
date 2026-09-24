import pytest

from my_project.core import word_count


def test_counts_are_case_insensitive_and_ignore_punctuation() -> None:
    assert word_count("Data, data. DATA! pipeline") == [("data", 3), ("pipeline", 1)]


def test_top_limits_the_result() -> None:
    assert word_count("a a a b b c", top=2) == [("a", 3), ("b", 2)]


def test_empty_text_returns_empty_list() -> None:
    assert word_count("   ") == []


@pytest.mark.parametrize("top", [0, -3])
def test_invalid_top_raises(top: int) -> None:
    with pytest.raises(ValueError, match="positive"):
        word_count("a b", top=top)
