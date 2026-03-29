test:
	uv run pytest

lint:
	uv run ruff check

lint_with_fix:
	uv run ruff check --fix