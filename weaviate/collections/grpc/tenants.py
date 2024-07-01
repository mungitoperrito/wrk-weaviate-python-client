from typing import Optional, Sequence, cast

from weaviate.collections.classes.config import ConsistencyLevel
from weaviate.collections.classes.tenants import TenantActivityStatus
from weaviate.collections.grpc.shared import _BaseGRPC

from weaviate.connect import ConnectionV4

from weaviate.proto.v1 import tenants_pb2


class _TenantsGRPC(_BaseGRPC):
    def __init__(
        self,
        connection: ConnectionV4,
        name: str,
        consistency_level: Optional[ConsistencyLevel],
    ):
        super().__init__(connection, consistency_level)
        self._name: str = name

    async def get(self, names: Optional[Sequence[str]]) -> tenants_pb2.TenantsGetReply:
        assert self._connection.grpc_stub is not None, "gRPC stub is not initialized"

        request = tenants_pb2.TenantsGetRequest(
            collection=self._name,
            names=tenants_pb2.TenantNames(values=names) if names is not None else None,
        )
        res = await self._connection.grpc_stub.TenantsGet(
            request,
            metadata=self._connection.grpc_headers(),
            timeout=self._connection.timeout_config.query,
        )
        return cast(tenants_pb2.TenantsGetReply, res)

    def map_activity_status(self, status: tenants_pb2.TenantActivityStatus) -> TenantActivityStatus:
        if status == tenants_pb2.TENANT_ACTIVITY_STATUS_COLD:
            return TenantActivityStatus.COLD
        if status == tenants_pb2.TENANT_ACTIVITY_STATUS_HOT:
            return TenantActivityStatus.HOT
        if status == tenants_pb2.TENANT_ACTIVITY_STATUS_FROZEN:
            return TenantActivityStatus.FROZEN
        if status == tenants_pb2.TENANT_ACTIVITY_STATUS_FREEZING:
            return TenantActivityStatus.FREEZING
        if status == tenants_pb2.TENANT_ACTIVITY_STATUS_UNFREEZING:
            return TenantActivityStatus.UNFREEZING
        if status == tenants_pb2.TENANT_ACTIVITY_STATUS_UNFROZEN:
            return TenantActivityStatus.UNFROZEN
        raise ValueError(f"Unknown TenantActivityStatus: {status}")
