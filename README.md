# P&ID Parsing: From Engineering Drawings to Structured Graphs

A collaborative capstone research repository for extracting symbols, text, lines
and eventually connectivity graphs from Piping and Instrumentation Diagrams.
The goal is reproducible independent baselines followed by contract-based integration.

## Architecture and ownership

This is a modular monolith. Three researchers can develop independent modules:

| Module | Responsibilities | Future output |
| --- | --- | --- |
| Symbols | Dataset handling, preprocessing, detection, postprocessing, evaluation | Localized equipment and instrument candidates |
| Text | Dataset handling, preprocessing, detection, recognition, evaluation | Text regions and recognized strings |
| Lines | Dataset handling, preprocessing, line detection, topology, evaluation | Segments, junctions and connectivity candidates |

Each module owns its internal schemas and preprocessing. Adapters will translate
results into integration artifacts in original-image coordinates. Core provides
image identity, geometry, transformations and a generic inference Protocol.
Integration will associate artifacts; graph will build, validate and export
connectivity. The pipeline will coordinate services without implementing algorithms.

## Repository structure

```text
configs/                  Reserved dataset/module configuration
data/                    raw, interim/{symbols,text,lines}, processed, samples
src/pid_parser/
  core/                   Implemented metadata, geometry, transforms, Protocol
  symbols/                datasets, preprocessing, models, postprocessing
  text/                   datasets, preprocessing, detection, recognition, postprocessing
  lines/                  datasets, preprocessing, detection, postprocessing, topology
  integration/            Reserved contracts and association packages
  graph/                  Reserved graph package
  pipeline/               Reserved orchestration package
  evaluation/             Reserved evaluation package
scripts/                  data, train, inference, evaluate, visualize workflow plans
notebooks/                symbols, text, lines
experiments/              symbols, text, lines; generated artifacts ignored
outputs/                  Generated outputs (ignored)
apps/demo/                Future demo
tests/                   unit, integration, fixtures
docs/                    Architecture, contracts, interfaces, development, Git workflow
.github/workflows/ci.yml  Lightweight CPU checks
```

## Environment setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) first.
From the repository root, with Python 3.11+ available:

```sh
uv sync --locked --group dev
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
```

`uv` creates `.venv` and installs the package in editable mode. `.python-version`
selects 3.11. To use 3.12, add `--python 3.12` to both `uv sync` and `uv run`
commands.
`uv sync --locked --no-default-groups` installs only the lightweight base environment.
Optional CV tools: `uv sync --locked --group dev --extra research` installs NumPy
and headless OpenCV. PyTorch, YOLO, PaddleOCR, NetworkX, Shapely and Streamlit are
future choices, deliberately absent from mandatory dependencies. No setup command
loads weights or datasets. Commit `uv.lock` for reproducible collaboration.

## Development workflow

Work from `dev` on `feature/<module>-<task>`. Keep algorithms under `src/pid_parser/`,
add tests for implemented behavior, and document dataset provenance and coordinates.
Run the checks above before requesting review. `make check` is optional shorthand
when Make is installed; the uv commands work in PowerShell too.
See [development](docs/development.md) and [Git workflow](docs/git_workflow.md).

## Current status and milestones

Implemented: installable packages; validated image metadata and finite geometry;
invertible axis-aligned scale/offset bookkeeping; generic inference Protocol;
tests, Ruff, CI and documentation. Reserved package directories mark future work;
services, schemas, adapters and algorithms will be added when implemented.

1. Agree dataset provenance, splits, annotation formats and baseline evaluation.
2. Build independent symbol, text and line baselines with module-owned schemas.
3. Define integration contracts from real outputs and implement tested adapters.
4. Research association, graph reconstruction and connectivity evaluation.
5. Add orchestration, exports and a demo after end-to-end behavior exists.

Read [architecture](docs/architecture.md), [data contracts](docs/data_contract.md)
and [module interfaces](docs/module_interfaces.md) before extending boundaries.
Do not commit datasets, credentials, weights or generated predictions. Store small,
licensed synthetic fixtures under `tests/fixtures/`.
