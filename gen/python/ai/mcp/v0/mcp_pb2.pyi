from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ("id", "correlation_id", "source_id", "destination_id", "destination_service", "passport_token", "error", "init_request", "init_ack", "ping", "pong", "list_tools_request", "call_tool_request", "list_tools_response", "call_tool_response")
    ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_SERVICE_FIELD_NUMBER: _ClassVar[int]
    PASSPORT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INIT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    INIT_ACK_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    PONG_FIELD_NUMBER: _ClassVar[int]
    LIST_TOOLS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CALL_TOOL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LIST_TOOLS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CALL_TOOL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    id: str
    correlation_id: str
    source_id: str
    destination_id: str
    destination_service: str
    passport_token: str
    error: Error
    init_request: InitRequest
    init_ack: InitAck
    ping: Ping
    pong: Pong
    list_tools_request: ListToolsRequest
    call_tool_request: CallToolRequest
    list_tools_response: ListToolsResponse
    call_tool_response: CallToolResponse
    def __init__(self, id: _Optional[str] = ..., correlation_id: _Optional[str] = ..., source_id: _Optional[str] = ..., destination_id: _Optional[str] = ..., destination_service: _Optional[str] = ..., passport_token: _Optional[str] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., init_request: _Optional[_Union[InitRequest, _Mapping]] = ..., init_ack: _Optional[_Union[InitAck, _Mapping]] = ..., ping: _Optional[_Union[Ping, _Mapping]] = ..., pong: _Optional[_Union[Pong, _Mapping]] = ..., list_tools_request: _Optional[_Union[ListToolsRequest, _Mapping]] = ..., call_tool_request: _Optional[_Union[CallToolRequest, _Mapping]] = ..., list_tools_response: _Optional[_Union[ListToolsResponse, _Mapping]] = ..., call_tool_response: _Optional[_Union[CallToolResponse, _Mapping]] = ...) -> None: ...

class InitRequest(_message.Message):
    __slots__ = ("name", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class InitAck(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Ping(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Pong(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListToolsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListToolsResponse(_message.Message):
    __slots__ = ("tools",)
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedCompositeFieldContainer[Tool]
    def __init__(self, tools: _Optional[_Iterable[_Union[Tool, _Mapping]]] = ...) -> None: ...

class Tool(_message.Message):
    __slots__ = ("name", "description", "parameters")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    parameters: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CallToolRequest(_message.Message):
    __slots__ = ("tool", "arguments")
    TOOL_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    tool: str
    arguments: _struct_pb2.Struct
    def __init__(self, tool: _Optional[str] = ..., arguments: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CallToolResponse(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: str
    error: Error
    def __init__(self, result: _Optional[str] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
