from weaviate.proto.v1 import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class TenantActivityStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TENANT_ACTIVITY_STATUS_UNSPECIFIED: _ClassVar[TenantActivityStatus]
    TENANT_ACTIVITY_STATUS_HOT: _ClassVar[TenantActivityStatus]
    TENANT_ACTIVITY_STATUS_COLD: _ClassVar[TenantActivityStatus]
    TENANT_ACTIVITY_STATUS_WARM: _ClassVar[TenantActivityStatus]
    TENANT_ACTIVITY_STATUS_FROZEN: _ClassVar[TenantActivityStatus]

TENANT_ACTIVITY_STATUS_UNSPECIFIED: TenantActivityStatus
TENANT_ACTIVITY_STATUS_HOT: TenantActivityStatus
TENANT_ACTIVITY_STATUS_COLD: TenantActivityStatus
TENANT_ACTIVITY_STATUS_WARM: TenantActivityStatus
TENANT_ACTIVITY_STATUS_FROZEN: TenantActivityStatus

class TenantsGetRequest(_message.Message):
    __slots__ = ("collection", "consistency_level", "names")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    collection: str
    consistency_level: _base_pb2.ConsistencyLevel
    names: TenantNames
    def __init__(
        self,
        collection: _Optional[str] = ...,
        consistency_level: _Optional[_Union[_base_pb2.ConsistencyLevel, str]] = ...,
        names: _Optional[_Union[TenantNames, _Mapping]] = ...,
    ) -> None: ...

class TenantNames(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class TenantsGetReply(_message.Message):
    __slots__ = ("took", "tenants")
    TOOK_FIELD_NUMBER: _ClassVar[int]
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    took: float
    tenants: _containers.RepeatedCompositeFieldContainer[Tenant]
    def __init__(
        self,
        took: _Optional[float] = ...,
        tenants: _Optional[_Iterable[_Union[Tenant, _Mapping]]] = ...,
    ) -> None: ...

class Tenant(_message.Message):
    __slots__ = ("name", "activity_status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    activity_status: TenantActivityStatus
    def __init__(
        self,
        name: _Optional[str] = ...,
        activity_status: _Optional[_Union[TenantActivityStatus, str]] = ...,
    ) -> None: ...
