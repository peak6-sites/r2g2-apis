from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IndexFile(_message.Message):
    __slots__ = ("store_id", "name", "upload_time", "directory_info", "file_info")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[IndexFile.State]
        INDEXING: _ClassVar[IndexFile.State]
        INDEXED: _ClassVar[IndexFile.State]
        FAILED: _ClassVar[IndexFile.State]
    STATE_UNSPECIFIED: IndexFile.State
    INDEXING: IndexFile.State
    INDEXED: IndexFile.State
    FAILED: IndexFile.State
    class DirectoryInfo(_message.Message):
        __slots__ = ("states",)
        class StatesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int
            def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
        STATES_FIELD_NUMBER: _ClassVar[int]
        states: _containers.ScalarMap[str, int]
        def __init__(self, states: _Optional[_Mapping[str, int]] = ...) -> None: ...
    class FileInfo(_message.Message):
        __slots__ = ("md5", "state", "state_reason")
        MD5_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        STATE_REASON_FIELD_NUMBER: _ClassVar[int]
        md5: str
        state: IndexFile.State
        state_reason: str
        def __init__(self, md5: _Optional[str] = ..., state: _Optional[_Union[IndexFile.State, str]] = ..., state_reason: _Optional[str] = ...) -> None: ...
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TIME_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    name: str
    upload_time: _timestamp_pb2.Timestamp
    directory_info: IndexFile.DirectoryInfo
    file_info: IndexFile.FileInfo
    def __init__(self, store_id: _Optional[str] = ..., name: _Optional[str] = ..., upload_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., directory_info: _Optional[_Union[IndexFile.DirectoryInfo, _Mapping]] = ..., file_info: _Optional[_Union[IndexFile.FileInfo, _Mapping]] = ...) -> None: ...

class ListIndexFilesRequest(_message.Message):
    __slots__ = ("store_id", "directory", "recursive", "page_size", "page_token")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    directory: str
    recursive: bool
    page_size: int
    page_token: str
    def __init__(self, store_id: _Optional[str] = ..., directory: _Optional[str] = ..., recursive: bool = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListIndexFilesResponse(_message.Message):
    __slots__ = ("files", "next_page_token")
    FILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[IndexFile]
    next_page_token: str
    def __init__(self, files: _Optional[_Iterable[_Union[IndexFile, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
