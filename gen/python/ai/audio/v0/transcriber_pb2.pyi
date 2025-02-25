from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TranscribeRequest(_message.Message):
    __slots__ = ("inline_data", "file_data", "prompt")
    INLINE_DATA_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    inline_data: Blob
    file_data: FileData
    prompt: str
    def __init__(self, inline_data: _Optional[_Union[Blob, _Mapping]] = ..., file_data: _Optional[_Union[FileData, _Mapping]] = ..., prompt: _Optional[str] = ...) -> None: ...

class Blob(_message.Message):
    __slots__ = ("mime_type", "data")
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    data: bytes
    def __init__(self, mime_type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class FileData(_message.Message):
    __slots__ = ("mime_type", "uri")
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    uri: str
    def __init__(self, mime_type: _Optional[str] = ..., uri: _Optional[str] = ...) -> None: ...

class Transcription(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...
