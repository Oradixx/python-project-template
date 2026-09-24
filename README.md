# python-project-template

[![CI](https://github.com/Oradixx/python-project-template/actions/workflows/ci.yml/badge.svg)](https://github.com/Oradixx/python-project-template/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12%20%7C%203.13-blue)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A minimal, production-minded starting point for Python projects: one command to set up,
one command to run every check, and the same checks enforced in CI.

## Quick start

1. Click **Use this template → Create a new repository** on GitHub, then clone it.
2. Rename the placeholders and install everything:

   ```bash
   python scripts/rename_project.py my-new-project   # then delete scripts/
   uv lock
   make install
   ```

3. Check that everything is green:

   ```bash
   make check
   ```

Requires [uv](https://docs.astral.sh/uv/) (`brew install uv`). Docker is only needed for the image.

## What's inside

| Tool | Why it is here |
|---|---|
| **uv** | Creates the virtualenv, resolves and installs dependencies from a lockfile (`uv.lock`) — same versions on every machine and in CI, and much faster than pip. |
| **`src/` layout** | Tests run against the *installed* package, not the working directory, so packaging mistakes surface early. |
| **Ruff** | Linter + formatter in one tool (replaces flake8, isort, black, pyupgrade). |
| **mypy (strict)** | Catches type errors before runtime; type hints double as documentation. |
| **pytest + coverage** | Tests with a coverage report; the build fails under 80 %. |
| **pre-commit** | Runs Ruff, whitespace fixes, secret detection and `uv lock` on every commit, so bad code never reaches the repo. |
| **GitHub Actions** | Lint, type check, tests on Python 3.12 and 3.13, Docker build + smoke test on every push and PR. |
| **Dependabot** | Weekly PRs to keep Actions and dependencies up to date. |
| **Dockerfile** | Multi-stage build: dependencies installed with uv, only the virtualenv copied into a slim image, runs as a non-root user. |
| **Makefile** | Short, memorable commands — `make help` lists them all. |

## Commands

```text
make install       Create the venv, install deps and git hooks
make lint          Lint and check formatting (no changes)
make format        Auto-fix lint issues and format code
make typecheck     Static type checking
make test          Run tests with coverage
make check         Everything CI runs
make docker-build  Build the Docker image
make docker-run    Run the image (example: echo "a b a" | make docker-run)
make clean         Remove caches and build artefacts
```

## Project structure

```text
.
├── .github/
│   ├── workflows/ci.yml       # CI pipeline
│   └── dependabot.yml         # automated dependency updates
├── scripts/rename_project.py  # one-off: rename the placeholders
├── src/my_project/
│   ├── __init__.py
│   ├── cli.py                 # command-line entry point (`my-project`)
│   ├── core.py                # business logic — pure, easy to test
│   └── py.typed               # marks the package as typed
├── tests/
├── .pre-commit-config.yaml
├── Dockerfile
├── Makefile
└── pyproject.toml             # metadata, dependencies and all tool settings
```

The sample code (a word counter) only exists to show how the pieces fit together — replace it with your own.

## License

[MIT](LICENSE)
