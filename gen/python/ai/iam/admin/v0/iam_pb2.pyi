from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceAccount(_message.Message):
    __slots__ = ("client_id", "client_email", "display_name", "description", "credentials")
    class Credentials(_message.Message):
        __slots__ = ("type", "client_id", "client_secret", "audience", "token_uri")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        AUDIENCE_FIELD_NUMBER: _ClassVar[int]
        TOKEN_URI_FIELD_NUMBER: _ClassVar[int]
        type: str
        client_id: str
        client_secret: str
        audience: str
        token_uri: str
        def __init__(self, type: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., audience: _Optional[str] = ..., token_uri: _Optional[str] = ...) -> None: ...
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_email: str
    display_name: str
    description: str
    credentials: bytes
    def __init__(self, client_id: _Optional[str] = ..., client_email: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., credentials: _Optional[bytes] = ...) -> None: ...

class CreateServiceAccountRequest(_message.Message):
    __slots__ = ("display_name", "description")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    def __init__(self, display_name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GetServiceAccountRequest(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class ListServiceAccountsRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListServiceAccountsResponse(_message.Message):
    __slots__ = ("service_accounts", "next_page_token")
    SERVICE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    service_accounts: _containers.RepeatedCompositeFieldContainer[ServiceAccount]
    next_page_token: str
    def __init__(self, service_accounts: _Optional[_Iterable[_Union[ServiceAccount, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteServiceAccountRequest(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...
