# Development

Install Python 3.11+ and uv, then run from the repository root:

```sh
uv sync --locked --group dev
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
```

Use `uv run --locked ruff format .` to format changes. Make is optional:
`make setup`, `make lint`, `make test`, `make format`, `make check` wrap these commands.
CI runs the same checks on Python 3.11 and 3.12 without GPU or secrets.

Base dependency: Pydantic 2. Development group: pytest and Ruff. Optional
`research` extra: NumPy and headless OpenCV. Add framework extras only when a
baseline needs them and document platform constraints. For dependency updates,
edit pyproject.toml, run `uv lock`, review and commit both manifest and lockfile.
Normal setup uses the checked-in lockfile. Avoid installing all future frameworks.

Test coordinate edge cases and real implemented contracts; keep fixtures small,
synthetic or licensed, under `tests/fixtures/`. Integration tests must exercise
implemented behavior. No downloads are permitted in tests. Models, datasets and
credentials stay out of Git. Dataset directories and generated artifact roots
are ignored except scaffolding; ordinary fixture images remain trackable.

Use configs for future experiment configuration and notebooks for exploration.
Move reusable algorithms into packages, preserve dataset splits and random seeds,
and document evaluation definitions before reporting metrics. Record experiment
recipes in tracked README files; generated experiment outputs remain ignored.
There are no runnable training/inference/evaluation scripts yet; their directories
describe intended entry points. Add pipeline configuration when a configuration
loader exists. `apps/demo` is reserved for future work.
