from ai.type import list_pb2 as _list_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Store(_message.Message):
    __slots__ = ("id", "display_name", "managed_by", "owner", "owners", "uploaders", "viewers", "create_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MANAGED_BY_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    UPLOADERS_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    managed_by: str
    owner: str
    owners: _containers.RepeatedScalarFieldContainer[str]
    uploaders: _containers.RepeatedScalarFieldContainer[str]
    viewers: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., managed_by: _Optional[str] = ..., owner: _Optional[str] = ..., owners: _Optional[_Iterable[str]] = ..., uploaders: _Optional[_Iterable[str]] = ..., viewers: _Optional[_Iterable[str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EmbeddingConfig(_message.Message):
    __slots__ = ("model", "dimensions")
    class Model(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_UNSPECIFIED: _ClassVar[EmbeddingConfig.Model]
        OPENAI_TEXT_EMBEDDING_ADA_002: _ClassVar[EmbeddingConfig.Model]
        OPENAI_TEXT_EMBEDDING_3_SMALL: _ClassVar[EmbeddingConfig.Model]
        OPENAI_TEXT_EMBEDDING_3_LARGE: _ClassVar[EmbeddingConfig.Model]
    MODEL_UNSPECIFIED: EmbeddingConfig.Model
    OPENAI_TEXT_EMBEDDING_ADA_002: EmbeddingConfig.Model
    OPENAI_TEXT_EMBEDDING_3_SMALL: EmbeddingConfig.Model
    OPENAI_TEXT_EMBEDDING_3_LARGE: EmbeddingConfig.Model
    MODEL_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    model: EmbeddingConfig.Model
    dimensions: int
    def __init__(self, model: _Optional[_Union[EmbeddingConfig.Model, str]] = ..., dimensions: _Optional[int] = ...) -> None: ...

class ChunkingConfig(_message.Message):
    __slots__ = ("chunk_size", "chunk_overlap")
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_OVERLAP_FIELD_NUMBER: _ClassVar[int]
    chunk_size: int
    chunk_overlap: int
    def __init__(self, chunk_size: _Optional[int] = ..., chunk_overlap: _Optional[int] = ...) -> None: ...

class StoreConfig(_message.Message):
    __slots__ = ("name", "config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class GetStoreConfigRequest(_message.Message):
    __slots__ = ("store_id", "name")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    name: str
    def __init__(self, store_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CreateStoreRequest(_message.Message):
    __slots__ = ("id", "display_name", "chunking_config", "embedding_config", "owners", "uploaders", "viewers")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CHUNKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    UPLOADERS_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    chunking_config: ChunkingConfig
    embedding_config: EmbeddingConfig
    owners: _containers.RepeatedScalarFieldContainer[str]
    uploaders: _containers.RepeatedScalarFieldContainer[str]
    viewers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., chunking_config: _Optional[_Union[ChunkingConfig, _Mapping]] = ..., embedding_config: _Optional[_Union[EmbeddingConfig, _Mapping]] = ..., owners: _Optional[_Iterable[str]] = ..., uploaders: _Optional[_Iterable[str]] = ..., viewers: _Optional[_Iterable[str]] = ...) -> None: ...

class GetStoreRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListStoresRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListStoresResponse(_message.Message):
    __slots__ = ("stores",)
    STORES_FIELD_NUMBER: _ClassVar[int]
    stores: _containers.RepeatedCompositeFieldContainer[Store]
    def __init__(self, stores: _Optional[_Iterable[_Union[Store, _Mapping]]] = ...) -> None: ...

class UpdateStoreRequest(_message.Message):
    __slots__ = ("id", "display_name", "owners", "uploaders", "viewers")
    class ViewersList(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    UPLOADERS_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    owners: _list_pb2.StringList
    uploaders: _list_pb2.StringList
    viewers: UpdateStoreRequest.ViewersList
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., owners: _Optional[_Union[_list_pb2.StringList, _Mapping]] = ..., uploaders: _Optional[_Union[_list_pb2.StringList, _Mapping]] = ..., viewers: _Optional[_Union[UpdateStoreRequest.ViewersList, _Mapping]] = ...) -> None: ...

class DeleteStoreRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class File(_message.Message):
    __slots__ = ("store_id", "filename", "size", "upload_time", "url", "state", "state_reason")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[File.State]
        INDEXING: _ClassVar[File.State]
        DELETING: _ClassVar[File.State]
        INDEXED: _ClassVar[File.State]
        FAILED: _ClassVar[File.State]
    STATE_UNSPECIFIED: File.State
    INDEXING: File.State
    DELETING: File.State
    INDEXED: File.State
    FAILED: File.State
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TIME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_REASON_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    filename: str
    size: int
    upload_time: _timestamp_pb2.Timestamp
    url: str
    state: File.State
    state_reason: str
    def __init__(self, store_id: _Optional[str] = ..., filename: _Optional[str] = ..., size: _Optional[int] = ..., upload_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., url: _Optional[str] = ..., state: _Optional[_Union[File.State, str]] = ..., state_reason: _Optional[str] = ...) -> None: ...

class UploadFileRequest(_message.Message):
    __slots__ = ("store_id", "filename", "content_type", "source_url")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    filename: str
    content_type: str
    source_url: str
    def __init__(self, store_id: _Optional[str] = ..., filename: _Optional[str] = ..., content_type: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...

class UploadFileUnaryResponse(_message.Message):
    __slots__ = ("store_id", "filename", "url", "headers")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    filename: str
    url: str
    headers: _containers.ScalarMap[str, str]
    def __init__(self, store_id: _Optional[str] = ..., filename: _Optional[str] = ..., url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ...) -> None: ...

class UploadFileEvent(_message.Message):
    __slots__ = ("store_id", "filename", "allocated")
    class Allocated(_message.Message):
        __slots__ = ("url", "headers")
        class HeadersEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        URL_FIELD_NUMBER: _ClassVar[int]
        HEADERS_FIELD_NUMBER: _ClassVar[int]
        url: str
        headers: _containers.ScalarMap[str, str]
        def __init__(self, url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ...) -> None: ...
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    filename: str
    allocated: UploadFileEvent.Allocated
    def __init__(self, store_id: _Optional[str] = ..., filename: _Optional[str] = ..., allocated: _Optional[_Union[UploadFileEvent.Allocated, _Mapping]] = ...) -> None: ...

class GetFileRequest(_message.Message):
    __slots__ = ("store_id", "filename")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    filename: str
    def __init__(self, store_id: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class ListFilesRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class ListFilesResponse(_message.Message):
    __slots__ = ("files",)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[File]
    def __init__(self, files: _Optional[_Iterable[_Union[File, _Mapping]]] = ...) -> None: ...

class DeleteFileRequest(_message.Message):
    __slots__ = ("store_id", "filename")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    filename: str
    def __init__(self, store_id: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class TestStorePermissionsRequest(_message.Message):
    __slots__ = ("id", "permissions")
    ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class TestStorePermissionsResponse(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class FileIndexEvent(_message.Message):
    __slots__ = ("event_id", "event_type", "event_time", "data")
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[FileIndexEvent.EventType]
        INDEXING_STARTED: _ClassVar[FileIndexEvent.EventType]
        INDEXED: _ClassVar[FileIndexEvent.EventType]
        DELETED: _ClassVar[FileIndexEvent.EventType]
        FAILED: _ClassVar[FileIndexEvent.EventType]
    EVENT_TYPE_UNSPECIFIED: FileIndexEvent.EventType
    INDEXING_STARTED: FileIndexEvent.EventType
    INDEXED: FileIndexEvent.EventType
    DELETED: FileIndexEvent.EventType
    FAILED: FileIndexEvent.EventType
    class EventData(_message.Message):
        __slots__ = ("store_id", "filename", "size", "md5", "create_time", "reason")
        STORE_ID_FIELD_NUMBER: _ClassVar[int]
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        MD5_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        store_id: str
        filename: str
        size: int
        md5: str
        create_time: _timestamp_pb2.Timestamp
        reason: str
        def __init__(self, store_id: _Optional[str] = ..., filename: _Optional[str] = ..., size: _Optional[int] = ..., md5: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    event_type: FileIndexEvent.EventType
    event_time: _timestamp_pb2.Timestamp
    data: FileIndexEvent.EventData
    def __init__(self, event_id: _Optional[str] = ..., event_type: _Optional[_Union[FileIndexEvent.EventType, str]] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., data: _Optional[_Union[FileIndexEvent.EventData, _Mapping]] = ...) -> None: ...

class IndexJobEvent(_message.Message):
    __slots__ = ("event_id", "event_time", "job_requested", "job_started", "job_succeeded", "job_failed")
    class JobAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOB_ACTION_UNSPECIFIED: _ClassVar[IndexJobEvent.JobAction]
        INSERT: _ClassVar[IndexJobEvent.JobAction]
        DELETE: _ClassVar[IndexJobEvent.JobAction]
    JOB_ACTION_UNSPECIFIED: IndexJobEvent.JobAction
    INSERT: IndexJobEvent.JobAction
    DELETE: IndexJobEvent.JobAction
    class JobState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOB_STATE_UNSPECIFIED: _ClassVar[IndexJobEvent.JobState]
        PENDING: _ClassVar[IndexJobEvent.JobState]
        RUNNING: _ClassVar[IndexJobEvent.JobState]
        COMPLETED: _ClassVar[IndexJobEvent.JobState]
    JOB_STATE_UNSPECIFIED: IndexJobEvent.JobState
    PENDING: IndexJobEvent.JobState
    RUNNING: IndexJobEvent.JobState
    COMPLETED: IndexJobEvent.JobState
    class File(_message.Message):
        __slots__ = ("name", "md5", "create_time")
        NAME_FIELD_NUMBER: _ClassVar[int]
        MD5_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        name: str
        md5: str
        create_time: _timestamp_pb2.Timestamp
        def __init__(self, name: _Optional[str] = ..., md5: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Job(_message.Message):
        __slots__ = ("name", "batch_id", "action", "exec_name")
        NAME_FIELD_NUMBER: _ClassVar[int]
        BATCH_ID_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        EXEC_NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        batch_id: str
        action: IndexJobEvent.JobAction
        exec_name: str
        def __init__(self, name: _Optional[str] = ..., batch_id: _Optional[str] = ..., action: _Optional[_Union[IndexJobEvent.JobAction, str]] = ..., exec_name: _Optional[str] = ...) -> None: ...
    class JobRequested(_message.Message):
        __slots__ = ("store_id", "file", "job")
        STORE_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_FIELD_NUMBER: _ClassVar[int]
        JOB_FIELD_NUMBER: _ClassVar[int]
        store_id: str
        file: IndexJobEvent.File
        job: IndexJobEvent.Job
        def __init__(self, store_id: _Optional[str] = ..., file: _Optional[_Union[IndexJobEvent.File, _Mapping]] = ..., job: _Optional[_Union[IndexJobEvent.Job, _Mapping]] = ...) -> None: ...
    class JobStarted(_message.Message):
        __slots__ = ("store_id", "file", "job")
        STORE_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_FIELD_NUMBER: _ClassVar[int]
        JOB_FIELD_NUMBER: _ClassVar[int]
        store_id: str
        file: IndexJobEvent.File
        job: IndexJobEvent.Job
        def __init__(self, store_id: _Optional[str] = ..., file: _Optional[_Union[IndexJobEvent.File, _Mapping]] = ..., job: _Optional[_Union[IndexJobEvent.Job, _Mapping]] = ...) -> None: ...
    class JobSucceeded(_message.Message):
        __slots__ = ("store_id", "file", "job", "n_inserted", "n_deleted")
        STORE_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_FIELD_NUMBER: _ClassVar[int]
        JOB_FIELD_NUMBER: _ClassVar[int]
        N_INSERTED_FIELD_NUMBER: _ClassVar[int]
        N_DELETED_FIELD_NUMBER: _ClassVar[int]
        store_id: str
        file: IndexJobEvent.File
        job: IndexJobEvent.Job
        n_inserted: int
        n_deleted: int
        def __init__(self, store_id: _Optional[str] = ..., file: _Optional[_Union[IndexJobEvent.File, _Mapping]] = ..., job: _Optional[_Union[IndexJobEvent.Job, _Mapping]] = ..., n_inserted: _Optional[int] = ..., n_deleted: _Optional[int] = ...) -> None: ...
    class JobFailed(_message.Message):
        __slots__ = ("store_id", "file", "job", "failure_reason")
        STORE_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_FIELD_NUMBER: _ClassVar[int]
        JOB_FIELD_NUMBER: _ClassVar[int]
        FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
        store_id: str
        file: IndexJobEvent.File
        job: IndexJobEvent.Job
        failure_reason: str
        def __init__(self, store_id: _Optional[str] = ..., file: _Optional[_Union[IndexJobEvent.File, _Mapping]] = ..., job: _Optional[_Union[IndexJobEvent.Job, _Mapping]] = ..., failure_reason: _Optional[str] = ...) -> None: ...
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    JOB_STARTED_FIELD_NUMBER: _ClassVar[int]
    JOB_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    JOB_FAILED_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    event_time: _timestamp_pb2.Timestamp
    job_requested: IndexJobEvent.JobRequested
    job_started: IndexJobEvent.JobStarted
    job_succeeded: IndexJobEvent.JobSucceeded
    job_failed: IndexJobEvent.JobFailed
    def __init__(self, event_id: _Optional[str] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., job_requested: _Optional[_Union[IndexJobEvent.JobRequested, _Mapping]] = ..., job_started: _Optional[_Union[IndexJobEvent.JobStarted, _Mapping]] = ..., job_succeeded: _Optional[_Union[IndexJobEvent.JobSucceeded, _Mapping]] = ..., job_failed: _Optional[_Union[IndexJobEvent.JobFailed, _Mapping]] = ...) -> None: ...
