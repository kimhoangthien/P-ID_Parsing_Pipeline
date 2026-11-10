# Lines research

Own this module's dataset readers, preprocessing, algorithms, internal schemas,
postprocessing and evaluation methodology. Anticipated flow: `datasets -> preprocessing -> detection -> postprocessing -> topology`.
Add a service to coordinate this flow and an adapter to convert results into
integration artifacts when the first baseline is implemented.

Import shared geometry from `core`; do not import sibling research modules.
Choose internal schemas with the first baseline. Preserve source image identity
and the transform for every processed image or tile. Return original-image
coordinates at the adapter boundary. Keep framework imports in implementation
modules and load models explicitly. Evaluation entry points belong in
`pid_parser.evaluation.lines`; module-specific metric helpers can live here.
No trained model, predictions, or metrics are implemented yet.
