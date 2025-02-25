from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Model(_message.Message):
    __slots__ = ("name", "display_name", "description", "alias_for", "parameters", "supports_image_input", "supported_input_formats", "tags", "recommended", "launch_stage", "replacement", "features", "hidden", "disabled")
    class LaunchStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GA: _ClassVar[Model.LaunchStage]
        BETA: _ClassVar[Model.LaunchStage]
        DEPRECATED: _ClassVar[Model.LaunchStage]
    GA: Model.LaunchStage
    BETA: Model.LaunchStage
    DEPRECATED: Model.LaunchStage
    class InputFormats(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INPUT_FORMAT_UNSPECIFIED: _ClassVar[Model.InputFormats]
        TEXT: _ClassVar[Model.InputFormats]
        IMAGE: _ClassVar[Model.InputFormats]
    INPUT_FORMAT_UNSPECIFIED: Model.InputFormats
    TEXT: Model.InputFormats
    IMAGE: Model.InputFormats
    class Tag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TAG_UNSPECIFIED: _ClassVar[Model.Tag]
        CREATIVE_WRITING: _ClassVar[Model.Tag]
        CODING: _ClassVar[Model.Tag]
        FAST: _ClassVar[Model.Tag]
        ONLINE_ACCESS: _ClassVar[Model.Tag]
    TAG_UNSPECIFIED: Model.Tag
    CREATIVE_WRITING: Model.Tag
    CODING: Model.Tag
    FAST: Model.Tag
    ONLINE_ACCESS: Model.Tag
    class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEATURE_UNSPECIFIED: _ClassVar[Model.Feature]
        TOOL_CALL: _ClassVar[Model.Feature]
        JSON_SCHEMA: _ClassVar[Model.Feature]
    FEATURE_UNSPECIFIED: Model.Feature
    TOOL_CALL: Model.Feature
    JSON_SCHEMA: Model.Feature
    class Parameter(_message.Message):
        __slots__ = ("name", "default_value", "min_value", "max_value")
        class Value(_message.Message):
            __slots__ = ("string_value", "int_value", "double_value", "bool_value")
            STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
            INT_VALUE_FIELD_NUMBER: _ClassVar[int]
            DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
            BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
            string_value: str
            int_value: int
            double_value: float
            bool_value: bool
            def __init__(self, string_value: _Optional[str] = ..., int_value: _Optional[int] = ..., double_value: _Optional[float] = ..., bool_value: bool = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
        MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        default_value: Model.Parameter.Value
        min_value: Model.Parameter.Value
        max_value: Model.Parameter.Value
        def __init__(self, name: _Optional[str] = ..., default_value: _Optional[_Union[Model.Parameter.Value, _Mapping]] = ..., min_value: _Optional[_Union[Model.Parameter.Value, _Mapping]] = ..., max_value: _Optional[_Union[Model.Parameter.Value, _Mapping]] = ...) -> None: ...
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Model.Parameter
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Model.Parameter, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FOR_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_IMAGE_INPUT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_INPUT_FORMATS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    alias_for: str
    parameters: _containers.MessageMap[str, Model.Parameter]
    supports_image_input: bool
    supported_input_formats: _containers.RepeatedScalarFieldContainer[Model.InputFormats]
    tags: _containers.RepeatedScalarFieldContainer[Model.Tag]
    recommended: bool
    launch_stage: Model.LaunchStage
    replacement: str
    features: _containers.RepeatedScalarFieldContainer[Model.Feature]
    hidden: bool
    disabled: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., alias_for: _Optional[str] = ..., parameters: _Optional[_Mapping[str, Model.Parameter]] = ..., supports_image_input: bool = ..., supported_input_formats: _Optional[_Iterable[_Union[Model.InputFormats, str]]] = ..., tags: _Optional[_Iterable[_Union[Model.Tag, str]]] = ..., recommended: bool = ..., launch_stage: _Optional[_Union[Model.LaunchStage, str]] = ..., replacement: _Optional[str] = ..., features: _Optional[_Iterable[_Union[Model.Feature, str]]] = ..., hidden: bool = ..., disabled: bool = ...) -> None: ...
