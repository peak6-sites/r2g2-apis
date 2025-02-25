from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tool(_message.Message):
    __slots__ = ("name", "description", "parameters")
    class Parameter(_message.Message):
        __slots__ = ("name", "description", "type", "values", "required")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[Tool.Parameter.Type]
            STRING: _ClassVar[Tool.Parameter.Type]
            NUMBER: _ClassVar[Tool.Parameter.Type]
            BOOLEAN: _ClassVar[Tool.Parameter.Type]
            ENUM: _ClassVar[Tool.Parameter.Type]
        TYPE_UNSPECIFIED: Tool.Parameter.Type
        STRING: Tool.Parameter.Type
        NUMBER: Tool.Parameter.Type
        BOOLEAN: Tool.Parameter.Type
        ENUM: Tool.Parameter.Type
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        type: Tool.Parameter.Type
        values: _containers.RepeatedScalarFieldContainer[str]
        required: bool
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[Tool.Parameter.Type, str]] = ..., values: _Optional[_Iterable[str]] = ..., required: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    parameters: _containers.RepeatedCompositeFieldContainer[Tool.Parameter]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[Tool.Parameter, _Mapping]]] = ...) -> None: ...

class ToolCall(_message.Message):
    __slots__ = ("id", "tool_name", "arguments", "state", "error", "response")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ToolCall.State]
        RESPONSE_REQUIRED: _ClassVar[ToolCall.State]
        COMPLETED: _ClassVar[ToolCall.State]
    STATE_UNSPECIFIED: ToolCall.State
    RESPONSE_REQUIRED: ToolCall.State
    COMPLETED: ToolCall.State
    ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    id: str
    tool_name: str
    arguments: str
    state: ToolCall.State
    error: bool
    response: str
    def __init__(self, id: _Optional[str] = ..., tool_name: _Optional[str] = ..., arguments: _Optional[str] = ..., state: _Optional[_Union[ToolCall.State, str]] = ..., error: bool = ..., response: _Optional[str] = ...) -> None: ...
