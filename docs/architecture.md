# Architecture

Use a modular monolith with independent research ownership and small contracts.
Dependency direction (arrows mean imports):

```text
symbols, text, lines -> core
module adapters -> their module schemas + integration contracts + core
integration -> integration contracts + core
graph -> integration contracts + core
pipeline -> module service interfaces + adapters + integration + graph
```

Core never imports research modules. Research modules never import one another.
Integration never imports model frameworks or concrete model implementations.
Pipeline wiring may choose services, but preprocessing and algorithms stay in
module implementations. Import heavy frameworks only in their optional backends.

Each module owns datasets, preprocessing, internal results, postprocessing and
metric definitions. `evaluation/` provides a future home for public evaluation
entry points; module-specific helpers can remain within each module. No central
preprocessing stage is required. Record transforms per tile or processed image.

Integration contracts will be negotiated after baseline outputs exist. Association
will link text to symbols and lines to symbols; fusion will collect these results.
Graph building, validation and exporting are separate future responsibilities.
Reserved packages contain no speculative implementation files. Add concrete
modules when needed; use explicit NotImplementedError for unfinished public APIs.

Only shared geometry is implemented today. Axis-aligned transformations represent
scale and translation; affine rotation/shear may be added later with an explicit
representation and tests. Avoid speculative plugin registries or orchestration engines.
