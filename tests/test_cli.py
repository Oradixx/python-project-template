import io

import pytest

from my_project.cli import main


def test_cli_prints_most_frequent_words(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("sys.stdin", io.StringIO("etl etl elt"))
    assert main(["--top", "1"]) == 0
    assert capsys.readouterr().out.split() == ["2", "etl"]
