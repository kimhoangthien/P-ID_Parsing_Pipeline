"""Structural inference interface; modules keep their own input and result types."""

from typing import Protocol, TypeVar

InputT = TypeVar("InputT", contravariant=True)
ResultT = TypeVar("ResultT", covariant=True)


class InferenceModule(Protocol[InputT, ResultT]):
    """Implementations own loading, preprocessing, inference and postprocessing."""

    def infer(self, request: InputT, /) -> ResultT:
        """Infer one request; concrete implementations define batching and errors."""
        ...
