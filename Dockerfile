# syntax=docker/dockerfile:1
# Multi-stage build: dependencies are installed with uv in a "builder" image,
# then only the ready-to-run virtual environment is copied into a slim runtime image.

# ---------- builder ----------
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0

WORKDIR /app

# 1) Dependencies only — this layer stays cached until uv.lock changes.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

# 2) The project itself, installed as a regular (non-editable) package.
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-editable

# ---------- runtime ----------
FROM python:3.12-slim-bookworm

RUN groupadd --system app && useradd --system --gid app --create-home app

COPY --from=builder --chown=app:app /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

USER app
WORKDIR /home/app

ENTRYPOINT ["my-project"]
