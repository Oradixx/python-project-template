"""Rename the template placeholders after clicking "Use this template".

Usage:
    python scripts/rename_project.py my-new-project

It replaces ``my-project`` / ``my_project`` everywhere (package folder, imports,
pyproject.toml, Dockerfile, CI…), then you can delete this script.
Standard library only, so it runs before any dependency is installed.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD_DIST, OLD_PKG = "my-project", "my_project"
SKIP_DIRS = {".git", ".venv", "__pycache__", ".mypy_cache", ".ruff_cache", ".pytest_cache"}
TEXT_SUFFIXES = {".py", ".toml", ".md", ".yml", ".yaml", ".cfg", ".txt", ".lock", ""}


def main() -> int:
    if len(sys.argv) != 2 or not re.fullmatch(r"[a-z][a-z0-9-]*[a-z0-9]", sys.argv[1]):
        print("usage: python scripts/rename_project.py <new-name>  (lowercase, digits, dashes)")
        return 1
    new_dist = sys.argv[1]
    new_pkg = new_dist.replace("-", "_")

    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts) or not path.is_file():
            continue
        if path.suffix not in TEXT_SUFFIXES or path.resolve() == Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:  # binary file (e.g. .coverage): leave it alone
            continue
        updated = text.replace(OLD_DIST, new_dist).replace(OLD_PKG, new_pkg)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            print(f"updated  {path.relative_to(ROOT)}")

    old_dir, new_dir = ROOT / "src" / OLD_PKG, ROOT / "src" / new_pkg
    if old_dir.exists():
        old_dir.rename(new_dir)
        print(f"renamed  src/{OLD_PKG} -> src/{new_pkg}")

    print("\nDone. Next: `uv lock` then `make install`.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
