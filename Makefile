.DEFAULT_GOAL := help
IMAGE ?= my-project

.PHONY: help install lint format typecheck test check docker-build docker-run clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

install: ## Create the venv, install deps and git hooks
	uv sync
	uv run pre-commit install

lint: ## Lint and check formatting (no changes)
	uv run ruff check .
	uv run ruff format --check .

format: ## Auto-fix lint issues and format code
	uv run ruff check --fix .
	uv run ruff format .

typecheck: ## Static type checking
	uv run mypy

test: ## Run tests with coverage
	uv run pytest

check: lint typecheck test ## Everything CI runs

docker-build: ## Build the Docker image
	docker build -t $(IMAGE) .

docker-run: ## Run the image (example: echo "a b a" | make docker-run)
	docker run --rm -i $(IMAGE)

clean: ## Remove caches and build artefacts
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov dist build
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
