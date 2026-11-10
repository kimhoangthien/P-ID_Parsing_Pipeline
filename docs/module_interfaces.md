# Module interfaces

`core.interfaces.InferenceModule[InputT, ResultT]` is a structural Protocol with
`infer(request, /) -> ResultT`. It does not prescribe model loading, image payloads,
batching, bounding boxes or confidence scores. Each module chooses concrete types
when implementing its first baseline. A class can satisfy the Protocol without
inheriting from it. Services should load expensive resources explicitly, not at import.

Future service flow: module request -> module preprocessing -> backend inference
-> module postprocessing -> module result. Results must retain image identity and
coordinate provenance. Inference errors must be explicit; an empty result must
mean successful inference with no findings, not missing implementation.

Adapters will accept a module's result and image/transform context, returning
agreed integration artifacts. No adapter Protocol or artifact schema is imposed
before real output examples are available. Add adapter modules alongside real
module results; no adapter implementations exist yet.

Pipeline orchestration will inject configured services and adapters, run modules,
associate artifacts and call graph construction. It is future work. Independently
test each service with small local fixtures; test adapters with known transforms.
Core Protocol behavior is exercised with a test-local concrete metadata consumer,
which is not a model or fabricated research prediction.
