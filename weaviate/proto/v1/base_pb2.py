# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/base.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rv1/base.proto\x12\x0bweaviate.v1\x1a\x1cgoogle/protobuf/struct.proto\"T\n\x15NumberArrayProperties\x12\x12\n\x06values\x18\x01 \x03(\x01\x42\x02\x18\x01\x12\x11\n\tprop_name\x18\x02 \x01(\t\x12\x14\n\x0cvalues_bytes\x18\x03 \x01(\x0c\"7\n\x12IntArrayProperties\x12\x0e\n\x06values\x18\x01 \x03(\x03\x12\x11\n\tprop_name\x18\x02 \x01(\t\"8\n\x13TextArrayProperties\x12\x0e\n\x06values\x18\x01 \x03(\t\x12\x11\n\tprop_name\x18\x02 \x01(\t\";\n\x16\x42ooleanArrayProperties\x12\x0e\n\x06values\x18\x01 \x03(\x08\x12\x11\n\tprop_name\x18\x02 \x01(\t\"\xf1\x03\n\x15ObjectPropertiesValue\x12\x33\n\x12non_ref_properties\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x43\n\x17number_array_properties\x18\x02 \x03(\x0b\x32\".weaviate.v1.NumberArrayProperties\x12=\n\x14int_array_properties\x18\x03 \x03(\x0b\x32\x1f.weaviate.v1.IntArrayProperties\x12?\n\x15text_array_properties\x18\x04 \x03(\x0b\x32 .weaviate.v1.TextArrayProperties\x12\x45\n\x18\x62oolean_array_properties\x18\x05 \x03(\x0b\x32#.weaviate.v1.BooleanArrayProperties\x12\x38\n\x11object_properties\x18\x06 \x03(\x0b\x32\x1d.weaviate.v1.ObjectProperties\x12\x43\n\x17object_array_properties\x18\x07 \x03(\x0b\x32\".weaviate.v1.ObjectArrayProperties\x12\x18\n\x10\x65mpty_list_props\x18\n \x03(\t\"^\n\x15ObjectArrayProperties\x12\x32\n\x06values\x18\x01 \x03(\x0b\x32\".weaviate.v1.ObjectPropertiesValue\x12\x11\n\tprop_name\x18\x02 \x01(\t\"X\n\x10ObjectProperties\x12\x31\n\x05value\x18\x01 \x01(\x0b\x32\".weaviate.v1.ObjectPropertiesValue\x12\x11\n\tprop_name\x18\x02 \x01(\t\"\x1b\n\tTextArray\x12\x0e\n\x06values\x18\x01 \x03(\t\"\x1a\n\x08IntArray\x12\x0e\n\x06values\x18\x01 \x03(\x03\"\x1d\n\x0bNumberArray\x12\x0e\n\x06values\x18\x01 \x03(\x01\"\x1e\n\x0c\x42ooleanArray\x12\x0e\n\x06values\x18\x01 \x03(\x08\"\xfc\x06\n\x07\x46ilters\x12/\n\x08operator\x18\x01 \x01(\x0e\x32\x1d.weaviate.v1.Filters.Operator\x12\x0e\n\x02on\x18\x02 \x03(\tB\x02\x18\x01\x12%\n\x07\x66ilters\x18\x03 \x03(\x0b\x32\x14.weaviate.v1.Filters\x12\x14\n\nvalue_text\x18\x04 \x01(\tH\x00\x12\x13\n\tvalue_int\x18\x05 \x01(\x03H\x00\x12\x17\n\rvalue_boolean\x18\x06 \x01(\x08H\x00\x12\x16\n\x0cvalue_number\x18\x07 \x01(\x01H\x00\x12\x32\n\x10value_text_array\x18\t \x01(\x0b\x32\x16.weaviate.v1.TextArrayH\x00\x12\x30\n\x0fvalue_int_array\x18\n \x01(\x0b\x32\x15.weaviate.v1.IntArrayH\x00\x12\x38\n\x13value_boolean_array\x18\x0b \x01(\x0b\x32\x19.weaviate.v1.BooleanArrayH\x00\x12\x36\n\x12value_number_array\x18\x0c \x01(\x0b\x32\x18.weaviate.v1.NumberArrayH\x00\x12\x36\n\tvalue_geo\x18\r \x01(\x0b\x32!.weaviate.v1.GeoCoordinatesFilterH\x00\x12)\n\x06target\x18\x14 \x01(\x0b\x32\x19.weaviate.v1.FilterTarget\"\xe3\x02\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x12\n\x0eOPERATOR_EQUAL\x10\x01\x12\x16\n\x12OPERATOR_NOT_EQUAL\x10\x02\x12\x19\n\x15OPERATOR_GREATER_THAN\x10\x03\x12\x1f\n\x1bOPERATOR_GREATER_THAN_EQUAL\x10\x04\x12\x16\n\x12OPERATOR_LESS_THAN\x10\x05\x12\x1c\n\x18OPERATOR_LESS_THAN_EQUAL\x10\x06\x12\x10\n\x0cOPERATOR_AND\x10\x07\x12\x0f\n\x0bOPERATOR_OR\x10\x08\x12\x1d\n\x19OPERATOR_WITHIN_GEO_RANGE\x10\t\x12\x11\n\rOPERATOR_LIKE\x10\n\x12\x14\n\x10OPERATOR_IS_NULL\x10\x0b\x12\x19\n\x15OPERATOR_CONTAINS_ANY\x10\x0c\x12\x19\n\x15OPERATOR_CONTAINS_ALL\x10\rB\x0c\n\ntest_value\"T\n\x1b\x46ilterReferenceSingleTarget\x12\n\n\x02on\x18\x01 \x01(\t\x12)\n\x06target\x18\x02 \x01(\x0b\x32\x19.weaviate.v1.FilterTarget\"n\n\x1a\x46ilterReferenceMultiTarget\x12\n\n\x02on\x18\x01 \x01(\t\x12)\n\x06target\x18\x02 \x01(\x0b\x32\x19.weaviate.v1.FilterTarget\x12\x19\n\x11target_collection\x18\x03 \x01(\t\"\"\n\x14\x46ilterReferenceCount\x12\n\n\x02on\x18\x01 \x01(\t\"\xe4\x01\n\x0c\x46ilterTarget\x12\x12\n\x08property\x18\x01 \x01(\tH\x00\x12\x41\n\rsingle_target\x18\x02 \x01(\x0b\x32(.weaviate.v1.FilterReferenceSingleTargetH\x00\x12?\n\x0cmulti_target\x18\x03 \x01(\x0b\x32\'.weaviate.v1.FilterReferenceMultiTargetH\x00\x12\x32\n\x05\x63ount\x18\x04 \x01(\x0b\x32!.weaviate.v1.FilterReferenceCountH\x00\x42\x08\n\x06target\"M\n\x14GeoCoordinatesFilter\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12\x10\n\x08\x64istance\x18\x03 \x01(\x02\"<\n\x07Vectors\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x04\x12\x14\n\x0cvector_bytes\x18\x03 \x01(\x0c*\x89\x01\n\x10\x43onsistencyLevel\x12!\n\x1d\x43ONSISTENCY_LEVEL_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43ONSISTENCY_LEVEL_ONE\x10\x01\x12\x1c\n\x18\x43ONSISTENCY_LEVEL_QUORUM\x10\x02\x12\x19\n\x15\x43ONSISTENCY_LEVEL_ALL\x10\x03\x42n\n#io.weaviate.client.grpc.protocol.v1B\x11WeaviateProtoBaseZ4github.com/weaviate/weaviate/grpc/generated;protocolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.base_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#io.weaviate.client.grpc.protocol.v1B\021WeaviateProtoBaseZ4github.com/weaviate/weaviate/grpc/generated;protocol'
  _globals['_NUMBERARRAYPROPERTIES'].fields_by_name['values']._options = None
  _globals['_NUMBERARRAYPROPERTIES'].fields_by_name['values']._serialized_options = b'\030\001'
  _globals['_FILTERS'].fields_by_name['on']._options = None
  _globals['_FILTERS'].fields_by_name['on']._serialized_options = b'\030\001'
  _globals['_CONSISTENCYLEVEL']._serialized_start=2630
  _globals['_CONSISTENCYLEVEL']._serialized_end=2767
  _globals['_NUMBERARRAYPROPERTIES']._serialized_start=60
  _globals['_NUMBERARRAYPROPERTIES']._serialized_end=144
  _globals['_INTARRAYPROPERTIES']._serialized_start=146
  _globals['_INTARRAYPROPERTIES']._serialized_end=201
  _globals['_TEXTARRAYPROPERTIES']._serialized_start=203
  _globals['_TEXTARRAYPROPERTIES']._serialized_end=259
  _globals['_BOOLEANARRAYPROPERTIES']._serialized_start=261
  _globals['_BOOLEANARRAYPROPERTIES']._serialized_end=320
  _globals['_OBJECTPROPERTIESVALUE']._serialized_start=323
  _globals['_OBJECTPROPERTIESVALUE']._serialized_end=820
  _globals['_OBJECTARRAYPROPERTIES']._serialized_start=822
  _globals['_OBJECTARRAYPROPERTIES']._serialized_end=916
  _globals['_OBJECTPROPERTIES']._serialized_start=918
  _globals['_OBJECTPROPERTIES']._serialized_end=1006
  _globals['_TEXTARRAY']._serialized_start=1008
  _globals['_TEXTARRAY']._serialized_end=1035
  _globals['_INTARRAY']._serialized_start=1037
  _globals['_INTARRAY']._serialized_end=1063
  _globals['_NUMBERARRAY']._serialized_start=1065
  _globals['_NUMBERARRAY']._serialized_end=1094
  _globals['_BOOLEANARRAY']._serialized_start=1096
  _globals['_BOOLEANARRAY']._serialized_end=1126
  _globals['_FILTERS']._serialized_start=1129
  _globals['_FILTERS']._serialized_end=2021
  _globals['_FILTERS_OPERATOR']._serialized_start=1652
  _globals['_FILTERS_OPERATOR']._serialized_end=2007
  _globals['_FILTERREFERENCESINGLETARGET']._serialized_start=2023
  _globals['_FILTERREFERENCESINGLETARGET']._serialized_end=2107
  _globals['_FILTERREFERENCEMULTITARGET']._serialized_start=2109
  _globals['_FILTERREFERENCEMULTITARGET']._serialized_end=2219
  _globals['_FILTERREFERENCECOUNT']._serialized_start=2221
  _globals['_FILTERREFERENCECOUNT']._serialized_end=2255
  _globals['_FILTERTARGET']._serialized_start=2258
  _globals['_FILTERTARGET']._serialized_end=2486
  _globals['_GEOCOORDINATESFILTER']._serialized_start=2488
  _globals['_GEOCOORDINATESFILTER']._serialized_end=2565
  _globals['_VECTORS']._serialized_start=2567
  _globals['_VECTORS']._serialized_end=2627
# @@protoc_insertion_point(module_scope)
