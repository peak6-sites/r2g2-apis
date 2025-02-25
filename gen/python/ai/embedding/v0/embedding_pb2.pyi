from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEmbeddingRequest(_message.Message):
    __slots__ = ("model", "text")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    model: str
    text: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model: _Optional[str] = ..., text: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateEmbeddingResponse(_message.Message):
    __slots__ = ("embeddings",)
    EMBEDDINGS_FIELD_NUMBER: _ClassVar[int]
    embeddings: _containers.RepeatedCompositeFieldContainer[Embedding]
    def __init__(self, embeddings: _Optional[_Iterable[_Union[Embedding, _Mapping]]] = ...) -> None: ...

class Embedding(_message.Message):
    __slots__ = ("embedding",)
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    embedding: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, embedding: _Optional[_Iterable[float]] = ...) -> None: ...

class ComputeSimilarityRequest(_message.Message):
    __slots__ = ("model", "text_1", "text_2")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TEXT_1_FIELD_NUMBER: _ClassVar[int]
    TEXT_2_FIELD_NUMBER: _ClassVar[int]
    model: str
    text_1: str
    text_2: str
    def __init__(self, model: _Optional[str] = ..., text_1: _Optional[str] = ..., text_2: _Optional[str] = ...) -> None: ...

class ComputeSimilarityResponse(_message.Message):
    __slots__ = ("similarity",)
    SIMILARITY_FIELD_NUMBER: _ClassVar[int]
    similarity: float
    def __init__(self, similarity: _Optional[float] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]] = ...) -> None: ...

class Model(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
