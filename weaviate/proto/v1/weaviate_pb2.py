# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/weaviate.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11v1/weaviate.proto\x12\x0bweaviate.v1\x1a\x0ev1/batch.proto\x1a\x15v1/batch_delete.proto\x1a\x13v1/search_get.proto\x1a\x10v1/tenants.proto2\xbf\x02\n\x08Weaviate\x12@\n\x06Search\x12\x1a.weaviate.v1.SearchRequest\x1a\x18.weaviate.v1.SearchReply"\x00\x12R\n\x0c\x42\x61tchObjects\x12 .weaviate.v1.BatchObjectsRequest\x1a\x1e.weaviate.v1.BatchObjectsReply"\x00\x12O\n\x0b\x42\x61tchDelete\x12\x1f.weaviate.v1.BatchDeleteRequest\x1a\x1d.weaviate.v1.BatchDeleteReply"\x00\x12L\n\nTenantsGet\x12\x1e.weaviate.v1.TenantsGetRequest\x1a\x1c.weaviate.v1.TenantsGetReply"\x00\x42j\n#io.weaviate.client.grpc.protocol.v1B\rWeaviateProtoZ4github.com/weaviate/weaviate/grpc/generated;protocolb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.weaviate_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n#io.weaviate.client.grpc.protocol.v1B\rWeaviateProtoZ4github.com/weaviate/weaviate/grpc/generated;protocol"
    _globals["_WEAVIATE"]._serialized_start = 113
    _globals["_WEAVIATE"]._serialized_end = 432
# @@protoc_insertion_point(module_scope)
