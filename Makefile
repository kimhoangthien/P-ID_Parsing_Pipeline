.PHONY: setup test lint format check
setup:
	uv sync --locked --group dev
test:
	uv run --locked pytest
lint:
	uv run --locked ruff check .
format:
	uv run --locked ruff format .
check:
	uv run --locked ruff check .
	uv run --locked ruff format --check .
	uv run --locked pytest
