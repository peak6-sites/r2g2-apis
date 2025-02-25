from ai import model_pb2 as _model_pb2
from ai.type import list_pb2 as _list_pb2
from buf.validate import validate_pb2 as _validate_pb2
from ai.assistants.v0 import tools_pb2 as _tools_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SortOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_ORDER_UNSPECIFIED: _ClassVar[SortOrder]
    ASCENDING: _ClassVar[SortOrder]
    DESCENDING: _ClassVar[SortOrder]

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_UNSPECIFIED: _ClassVar[Role]
    USER: _ClassVar[Role]
    ASSISTANT: _ClassVar[Role]
SORT_ORDER_UNSPECIFIED: SortOrder
ASCENDING: SortOrder
DESCENDING: SortOrder
ROLE_UNSPECIFIED: Role
USER: Role
ASSISTANT: Role

class ListEnginesRequest(_message.Message):
    __slots__ = ("engine", "recommended", "input_formats", "tags")
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_FIELD_NUMBER: _ClassVar[int]
    INPUT_FORMATS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    engine: str
    recommended: bool
    input_formats: _containers.RepeatedScalarFieldContainer[_model_pb2.Model.InputFormats]
    tags: _containers.RepeatedScalarFieldContainer[_model_pb2.Model.Tag]
    def __init__(self, engine: _Optional[str] = ..., recommended: bool = ..., input_formats: _Optional[_Iterable[_Union[_model_pb2.Model.InputFormats, str]]] = ..., tags: _Optional[_Iterable[_Union[_model_pb2.Model.Tag, str]]] = ...) -> None: ...

class ListEnginesResponse(_message.Message):
    __slots__ = ("engines",)
    class EngineDescriptor(_message.Message):
        __slots__ = ("engine", "models")
        ENGINE_FIELD_NUMBER: _ClassVar[int]
        MODELS_FIELD_NUMBER: _ClassVar[int]
        engine: str
        models: _containers.RepeatedCompositeFieldContainer[_model_pb2.Model]
        def __init__(self, engine: _Optional[str] = ..., models: _Optional[_Iterable[_Union[_model_pb2.Model, _Mapping]]] = ...) -> None: ...
    ENGINES_FIELD_NUMBER: _ClassVar[int]
    engines: _containers.RepeatedCompositeFieldContainer[ListEnginesResponse.EngineDescriptor]
    def __init__(self, engines: _Optional[_Iterable[_Union[ListEnginesResponse.EngineDescriptor, _Mapping]]] = ...) -> None: ...

class Assistant(_message.Message):
    __slots__ = ("id", "display_name", "description", "store_id", "engine", "model", "instructions", "model_settings", "retrieval_settings", "citations_enabled", "sub_assistants", "sub_assistants_as_tools", "tools", "mcp_server", "response_json_schema", "certified", "owner", "owners", "uploaders", "viewers", "metadata", "create_time")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSISTANTS_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSISTANTS_AS_TOOLS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    CERTIFIED_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    UPLOADERS_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    description: str
    store_id: str
    engine: str
    model: str
    instructions: str
    model_settings: ModelSettings
    retrieval_settings: RetrievalSettings
    citations_enabled: bool
    sub_assistants: _containers.RepeatedScalarFieldContainer[str]
    sub_assistants_as_tools: bool
    tools: _containers.RepeatedCompositeFieldContainer[_tools_pb2.Tool]
    mcp_server: str
    response_json_schema: JsonSchemaResponseFormat
    certified: bool
    owner: str
    owners: _containers.RepeatedScalarFieldContainer[str]
    uploaders: _containers.RepeatedScalarFieldContainer[str]
    viewers: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., store_id: _Optional[str] = ..., engine: _Optional[str] = ..., model: _Optional[str] = ..., instructions: _Optional[str] = ..., model_settings: _Optional[_Union[ModelSettings, _Mapping]] = ..., retrieval_settings: _Optional[_Union[RetrievalSettings, _Mapping]] = ..., citations_enabled: bool = ..., sub_assistants: _Optional[_Iterable[str]] = ..., sub_assistants_as_tools: bool = ..., tools: _Optional[_Iterable[_Union[_tools_pb2.Tool, _Mapping]]] = ..., mcp_server: _Optional[str] = ..., response_json_schema: _Optional[_Union[JsonSchemaResponseFormat, _Mapping]] = ..., certified: bool = ..., owner: _Optional[str] = ..., owners: _Optional[_Iterable[str]] = ..., uploaders: _Optional[_Iterable[str]] = ..., viewers: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class JsonSchemaResponseFormat(_message.Message):
    __slots__ = ("schema", "description")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    schema: str
    description: str
    def __init__(self, schema: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateAssistantRequest(_message.Message):
    __slots__ = ("display_name", "description", "store_id", "engine", "model", "instructions", "model_settings", "retrieval_settings", "citations_enabled", "sub_assistants", "sub_assistants_as_tools", "tools", "mcp_server", "response_json_schema", "owners", "uploaders", "viewers", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSISTANTS_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSISTANTS_AS_TOOLS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    UPLOADERS_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    store_id: str
    engine: str
    model: str
    instructions: str
    model_settings: ModelSettings
    retrieval_settings: RetrievalSettings
    citations_enabled: bool
    sub_assistants: _containers.RepeatedScalarFieldContainer[str]
    sub_assistants_as_tools: bool
    tools: _containers.RepeatedCompositeFieldContainer[_tools_pb2.Tool]
    mcp_server: str
    response_json_schema: JsonSchemaResponseFormat
    owners: _containers.RepeatedScalarFieldContainer[str]
    uploaders: _containers.RepeatedScalarFieldContainer[str]
    viewers: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, display_name: _Optional[str] = ..., description: _Optional[str] = ..., store_id: _Optional[str] = ..., engine: _Optional[str] = ..., model: _Optional[str] = ..., instructions: _Optional[str] = ..., model_settings: _Optional[_Union[ModelSettings, _Mapping]] = ..., retrieval_settings: _Optional[_Union[RetrievalSettings, _Mapping]] = ..., citations_enabled: bool = ..., sub_assistants: _Optional[_Iterable[str]] = ..., sub_assistants_as_tools: bool = ..., tools: _Optional[_Iterable[_Union[_tools_pb2.Tool, _Mapping]]] = ..., mcp_server: _Optional[str] = ..., response_json_schema: _Optional[_Union[JsonSchemaResponseFormat, _Mapping]] = ..., owners: _Optional[_Iterable[str]] = ..., uploaders: _Optional[_Iterable[str]] = ..., viewers: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetAssistantRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListAssistantsRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "store_id", "metadata", "certified")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CERTIFIED_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    store_id: str
    metadata: _containers.ScalarMap[str, str]
    certified: bool
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., store_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., certified: bool = ...) -> None: ...

class ListAssistantsResponse(_message.Message):
    __slots__ = ("assistants", "next_page_token")
    ASSISTANTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    assistants: _containers.RepeatedCompositeFieldContainer[Assistant]
    next_page_token: str
    def __init__(self, assistants: _Optional[_Iterable[_Union[Assistant, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateAssistantRequest(_message.Message):
    __slots__ = ("id", "display_name", "description", "store_id", "engine", "model", "instructions", "model_settings", "retrieval_settings", "citations_enabled", "sub_assistants", "sub_assistants_as_tools", "metadata", "tools", "mcp_server", "response_json_schema", "owners", "uploaders", "viewers")
    class OwnerList(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
    class UploaderList(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
    class ViewerList(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
    class Metadata(_message.Message):
        __slots__ = ("values",)
        class ValuesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.ScalarMap[str, str]
        def __init__(self, values: _Optional[_Mapping[str, str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSISTANTS_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSISTANTS_AS_TOOLS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    UPLOADERS_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    description: str
    store_id: str
    engine: str
    model: str
    instructions: str
    model_settings: ModelSettings
    retrieval_settings: RetrievalSettings
    citations_enabled: bool
    sub_assistants: _list_pb2.StringList
    sub_assistants_as_tools: bool
    metadata: UpdateAssistantRequest.Metadata
    tools: Tools
    mcp_server: str
    response_json_schema: JsonSchemaResponseFormat
    owners: UpdateAssistantRequest.OwnerList
    uploaders: UpdateAssistantRequest.UploaderList
    viewers: UpdateAssistantRequest.ViewerList
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., store_id: _Optional[str] = ..., engine: _Optional[str] = ..., model: _Optional[str] = ..., instructions: _Optional[str] = ..., model_settings: _Optional[_Union[ModelSettings, _Mapping]] = ..., retrieval_settings: _Optional[_Union[RetrievalSettings, _Mapping]] = ..., citations_enabled: bool = ..., sub_assistants: _Optional[_Union[_list_pb2.StringList, _Mapping]] = ..., sub_assistants_as_tools: bool = ..., metadata: _Optional[_Union[UpdateAssistantRequest.Metadata, _Mapping]] = ..., tools: _Optional[_Union[Tools, _Mapping]] = ..., mcp_server: _Optional[str] = ..., response_json_schema: _Optional[_Union[JsonSchemaResponseFormat, _Mapping]] = ..., owners: _Optional[_Union[UpdateAssistantRequest.OwnerList, _Mapping]] = ..., uploaders: _Optional[_Union[UpdateAssistantRequest.UploaderList, _Mapping]] = ..., viewers: _Optional[_Union[UpdateAssistantRequest.ViewerList, _Mapping]] = ...) -> None: ...

class Tools(_message.Message):
    __slots__ = ("tools",)
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedCompositeFieldContainer[_tools_pb2.Tool]
    def __init__(self, tools: _Optional[_Iterable[_Union[_tools_pb2.Tool, _Mapping]]] = ...) -> None: ...

class DeleteAssistantRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class TestAssistantPermissionsRequest(_message.Message):
    __slots__ = ("id", "permissions")
    ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class TestAssistantPermissionsResponse(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class Thread(_message.Message):
    __slots__ = ("id", "description", "origin", "metadata", "create_time")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateThreadRequest(_message.Message):
    __slots__ = ("description", "messages", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    description: str
    messages: _containers.RepeatedCompositeFieldContainer[CreateMessageRequest]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, description: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[CreateMessageRequest, _Mapping]]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetThreadRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListThreadsRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "origin", "metadata", "order")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    order: SortOrder
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., order: _Optional[_Union[SortOrder, str]] = ...) -> None: ...

class ListThreadsResponse(_message.Message):
    __slots__ = ("threads", "next_page_token")
    THREADS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    threads: _containers.RepeatedCompositeFieldContainer[Thread]
    next_page_token: str
    def __init__(self, threads: _Optional[_Iterable[_Union[Thread, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateThreadRequest(_message.Message):
    __slots__ = ("id", "description", "metadata")
    class Metadata(_message.Message):
        __slots__ = ("values",)
        class ValuesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.ScalarMap[str, str]
        def __init__(self, values: _Optional[_Mapping[str, str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    metadata: UpdateThreadRequest.Metadata
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Union[UpdateThreadRequest.Metadata, _Mapping]] = ...) -> None: ...

class DeleteThreadRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ShareThreadRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class File(_message.Message):
    __slots__ = ("ref",)
    REF_FIELD_NUMBER: _ClassVar[int]
    ref: str
    def __init__(self, ref: _Optional[str] = ...) -> None: ...

class Image(_message.Message):
    __slots__ = ("url", "data")
    class Data(_message.Message):
        __slots__ = ("media_type", "data")
        MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        media_type: str
        data: bytes
        def __init__(self, media_type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...
    URL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    url: str
    data: Image.Data
    def __init__(self, url: _Optional[str] = ..., data: _Optional[_Union[Image.Data, _Mapping]] = ...) -> None: ...

class MessageContent(_message.Message):
    __slots__ = ("text", "image", "file", "citations")
    class Citation(_message.Message):
        __slots__ = ("tag", "display_name", "url", "metadata")
        class MetadataEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        TAG_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        tag: str
        display_name: str
        url: str
        metadata: _containers.ScalarMap[str, str]
        def __init__(self, tag: _Optional[str] = ..., display_name: _Optional[str] = ..., url: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_FIELD_NUMBER: _ClassVar[int]
    text: str
    image: Image
    file: File
    citations: _containers.RepeatedCompositeFieldContainer[MessageContent.Citation]
    def __init__(self, text: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., file: _Optional[_Union[File, _Mapping]] = ..., citations: _Optional[_Iterable[_Union[MessageContent.Citation, _Mapping]]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("id", "role", "content", "metadata", "state", "create_time", "modify_time", "run_id")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Message.State]
        PENDING: _ClassVar[Message.State]
        GENERATING: _ClassVar[Message.State]
        COMPLETED: _ClassVar[Message.State]
    STATE_UNSPECIFIED: Message.State
    PENDING: Message.State
    GENERATING: Message.State
    COMPLETED: Message.State
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    role: Role
    content: _containers.RepeatedCompositeFieldContainer[MessageContent]
    metadata: _containers.ScalarMap[str, str]
    state: Message.State
    create_time: _timestamp_pb2.Timestamp
    modify_time: _timestamp_pb2.Timestamp
    run_id: str
    def __init__(self, id: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., content: _Optional[_Iterable[_Union[MessageContent, _Mapping]]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Union[Message.State, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., modify_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., run_id: _Optional[str] = ...) -> None: ...

class ModelSettings(_message.Message):
    __slots__ = ("max_tokens", "temperature")
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    max_tokens: int
    temperature: float
    def __init__(self, max_tokens: _Optional[int] = ..., temperature: _Optional[float] = ...) -> None: ...

class RetrievalSettings(_message.Message):
    __slots__ = ("top_k", "min_relevance_score")
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    MIN_RELEVANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    top_k: int
    min_relevance_score: float
    def __init__(self, top_k: _Optional[int] = ..., min_relevance_score: _Optional[float] = ...) -> None: ...

class CreateMessageRequest(_message.Message):
    __slots__ = ("thread_id", "role", "content", "attachments", "metadata")
    class Attachment(_message.Message):
        __slots__ = ("image", "file")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        FILE_FIELD_NUMBER: _ClassVar[int]
        image: Image
        file: File
        def __init__(self, image: _Optional[_Union[Image, _Mapping]] = ..., file: _Optional[_Union[File, _Mapping]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    thread_id: str
    role: Role
    content: str
    attachments: _containers.RepeatedCompositeFieldContainer[CreateMessageRequest.Attachment]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, thread_id: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., content: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[CreateMessageRequest.Attachment, _Mapping]]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetMessageRequest(_message.Message):
    __slots__ = ("thread_id", "message_id")
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    thread_id: str
    message_id: str
    def __init__(self, thread_id: _Optional[str] = ..., message_id: _Optional[str] = ...) -> None: ...

class ListMessagesRequest(_message.Message):
    __slots__ = ("thread_id", "page_size", "page_token", "order", "run_id", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    thread_id: str
    page_size: int
    page_token: str
    order: SortOrder
    run_id: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, thread_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order: _Optional[_Union[SortOrder, str]] = ..., run_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListMessagesResponse(_message.Message):
    __slots__ = ("messages", "next_page_token")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    next_page_token: str
    def __init__(self, messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SourceFact(_message.Message):
    __slots__ = ("text", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    text: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, text: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Run(_message.Message):
    __slots__ = ("id", "thread_id", "assistant_id", "store_id", "engine", "model", "instructions", "model_settings", "retrieval_settings", "citations_enabled", "sub_assistants", "child_run_ids", "sub_assistants_as_tools", "metadata", "tools", "mcp_server", "tool_calls", "response_json_schema", "state", "failure_reason", "context_documents", "source_facts", "citations", "create_time", "start_time", "end_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Run.State]
        PENDING: _ClassVar[Run.State]
        RUNNING: _ClassVar[Run.State]
        SUCCEEDED: _ClassVar[Run.State]
        FAILED: _ClassVar[Run.State]
        TOOL_RESPONSE_REQUIRED: _ClassVar[Run.State]
    STATE_UNSPECIFIED: Run.State
    PENDING: Run.State
    RUNNING: Run.State
    SUCCEEDED: Run.State
    FAILED: Run.State
    TOOL_RESPONSE_REQUIRED: Run.State
    class Citation(_message.Message):
        __slots__ = ("position", "source")
        class Position(_message.Message):
            __slots__ = ("start_offset", "end_offset")
            START_OFFSET_FIELD_NUMBER: _ClassVar[int]
            END_OFFSET_FIELD_NUMBER: _ClassVar[int]
            start_offset: int
            end_offset: int
            def __init__(self, start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ...) -> None: ...
        POSITION_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        position: Run.Citation.Position
        source: int
        def __init__(self, position: _Optional[_Union[Run.Citation.Position, _Mapping]] = ..., source: _Optional[int] = ...) -> None: ...
    class ContextDocument(_message.Message):
        __slots__ = ("filename", "display_name", "url", "trailer")
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        TRAILER_FIELD_NUMBER: _ClassVar[int]
        filename: str
        display_name: str
        url: str
        trailer: str
        def __init__(self, filename: _Optional[str] = ..., display_name: _Optional[str] = ..., url: _Optional[str] = ..., trailer: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSISTANTS_FIELD_NUMBER: _ClassVar[int]
    CHILD_RUN_IDS_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSISTANTS_AS_TOOLS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FACTS_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    thread_id: str
    assistant_id: str
    store_id: str
    engine: str
    model: str
    instructions: str
    model_settings: ModelSettings
    retrieval_settings: RetrievalSettings
    citations_enabled: bool
    sub_assistants: _containers.RepeatedScalarFieldContainer[str]
    child_run_ids: _containers.RepeatedScalarFieldContainer[str]
    sub_assistants_as_tools: bool
    metadata: _containers.ScalarMap[str, str]
    tools: _containers.RepeatedCompositeFieldContainer[_tools_pb2.Tool]
    mcp_server: str
    tool_calls: _containers.RepeatedCompositeFieldContainer[_tools_pb2.ToolCall]
    response_json_schema: JsonSchemaResponseFormat
    state: Run.State
    failure_reason: str
    context_documents: _containers.RepeatedCompositeFieldContainer[Run.ContextDocument]
    source_facts: _containers.RepeatedCompositeFieldContainer[SourceFact]
    citations: _containers.RepeatedCompositeFieldContainer[Run.Citation]
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., thread_id: _Optional[str] = ..., assistant_id: _Optional[str] = ..., store_id: _Optional[str] = ..., engine: _Optional[str] = ..., model: _Optional[str] = ..., instructions: _Optional[str] = ..., model_settings: _Optional[_Union[ModelSettings, _Mapping]] = ..., retrieval_settings: _Optional[_Union[RetrievalSettings, _Mapping]] = ..., citations_enabled: bool = ..., sub_assistants: _Optional[_Iterable[str]] = ..., child_run_ids: _Optional[_Iterable[str]] = ..., sub_assistants_as_tools: bool = ..., metadata: _Optional[_Mapping[str, str]] = ..., tools: _Optional[_Iterable[_Union[_tools_pb2.Tool, _Mapping]]] = ..., mcp_server: _Optional[str] = ..., tool_calls: _Optional[_Iterable[_Union[_tools_pb2.ToolCall, _Mapping]]] = ..., response_json_schema: _Optional[_Union[JsonSchemaResponseFormat, _Mapping]] = ..., state: _Optional[_Union[Run.State, str]] = ..., failure_reason: _Optional[str] = ..., context_documents: _Optional[_Iterable[_Union[Run.ContextDocument, _Mapping]]] = ..., source_facts: _Optional[_Iterable[_Union[SourceFact, _Mapping]]] = ..., citations: _Optional[_Iterable[_Union[Run.Citation, _Mapping]]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateThreadAndRunRequest(_message.Message):
    __slots__ = ("thread", "assistant_id", "engine", "model", "instructions", "additional_instructions", "model_settings", "retrieval_settings", "citations_enabled", "tools", "mcp_server", "response_json_schema", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    THREAD_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    thread: CreateThreadRequest
    assistant_id: str
    engine: str
    model: str
    instructions: str
    additional_instructions: str
    model_settings: ModelSettings
    retrieval_settings: RetrievalSettings
    citations_enabled: bool
    tools: _containers.RepeatedCompositeFieldContainer[_tools_pb2.Tool]
    mcp_server: str
    response_json_schema: JsonSchemaResponseFormat
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, thread: _Optional[_Union[CreateThreadRequest, _Mapping]] = ..., assistant_id: _Optional[str] = ..., engine: _Optional[str] = ..., model: _Optional[str] = ..., instructions: _Optional[str] = ..., additional_instructions: _Optional[str] = ..., model_settings: _Optional[_Union[ModelSettings, _Mapping]] = ..., retrieval_settings: _Optional[_Union[RetrievalSettings, _Mapping]] = ..., citations_enabled: bool = ..., tools: _Optional[_Iterable[_Union[_tools_pb2.Tool, _Mapping]]] = ..., mcp_server: _Optional[str] = ..., response_json_schema: _Optional[_Union[JsonSchemaResponseFormat, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateRunRequest(_message.Message):
    __slots__ = ("thread_id", "assistant_id", "engine", "model", "instructions", "additional_instructions", "model_settings", "retrieval_settings", "citations_enabled", "tools", "mcp_server", "response_json_schema", "additional_messages", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    thread_id: str
    assistant_id: str
    engine: str
    model: str
    instructions: str
    additional_instructions: str
    model_settings: ModelSettings
    retrieval_settings: RetrievalSettings
    citations_enabled: bool
    tools: _containers.RepeatedCompositeFieldContainer[_tools_pb2.Tool]
    mcp_server: str
    response_json_schema: JsonSchemaResponseFormat
    additional_messages: _containers.RepeatedCompositeFieldContainer[CreateMessageRequest]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, thread_id: _Optional[str] = ..., assistant_id: _Optional[str] = ..., engine: _Optional[str] = ..., model: _Optional[str] = ..., instructions: _Optional[str] = ..., additional_instructions: _Optional[str] = ..., model_settings: _Optional[_Union[ModelSettings, _Mapping]] = ..., retrieval_settings: _Optional[_Union[RetrievalSettings, _Mapping]] = ..., citations_enabled: bool = ..., tools: _Optional[_Iterable[_Union[_tools_pb2.Tool, _Mapping]]] = ..., mcp_server: _Optional[str] = ..., response_json_schema: _Optional[_Union[JsonSchemaResponseFormat, _Mapping]] = ..., additional_messages: _Optional[_Iterable[_Union[CreateMessageRequest, _Mapping]]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetRunRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListRunsRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "assistant_id", "thread_id", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    assistant_id: str
    thread_id: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., assistant_id: _Optional[str] = ..., thread_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListRunsResponse(_message.Message):
    __slots__ = ("runs", "next_page_token")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[Run]
    next_page_token: str
    def __init__(self, runs: _Optional[_Iterable[_Union[Run, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteRunRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class StreamRunResultsRequest(_message.Message):
    __slots__ = ("run_id", "start_time")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    start_time: _timestamp_pb2.Timestamp
    def __init__(self, run_id: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StreamRunResultsResponse(_message.Message):
    __slots__ = ("message", "event_time")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    message: Message
    event_time: _timestamp_pb2.Timestamp
    def __init__(self, message: _Optional[_Union[Message, _Mapping]] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SubmitToolResponsesRequest(_message.Message):
    __slots__ = ("run_id", "responses")
    class ToolResponse(_message.Message):
        __slots__ = ("tool_call_id", "error", "text")
        TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        tool_call_id: str
        error: bool
        text: str
        def __init__(self, tool_call_id: _Optional[str] = ..., error: bool = ..., text: _Optional[str] = ...) -> None: ...
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    responses: _containers.RepeatedCompositeFieldContainer[SubmitToolResponsesRequest.ToolResponse]
    def __init__(self, run_id: _Optional[str] = ..., responses: _Optional[_Iterable[_Union[SubmitToolResponsesRequest.ToolResponse, _Mapping]]] = ...) -> None: ...

class CreateRunFeedbackRequest(_message.Message):
    __slots__ = ("run_id", "rating", "reason", "comment")
    class Rating(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RATING_UNSPECIFIED: _ClassVar[CreateRunFeedbackRequest.Rating]
        POSITIVE: _ClassVar[CreateRunFeedbackRequest.Rating]
        NEGATIVE: _ClassVar[CreateRunFeedbackRequest.Rating]
        NEUTRAL: _ClassVar[CreateRunFeedbackRequest.Rating]
    RATING_UNSPECIFIED: CreateRunFeedbackRequest.Rating
    POSITIVE: CreateRunFeedbackRequest.Rating
    NEGATIVE: CreateRunFeedbackRequest.Rating
    NEUTRAL: CreateRunFeedbackRequest.Rating
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    rating: CreateRunFeedbackRequest.Rating
    reason: str
    comment: str
    def __init__(self, run_id: _Optional[str] = ..., rating: _Optional[_Union[CreateRunFeedbackRequest.Rating, str]] = ..., reason: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class RunFeedback(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
