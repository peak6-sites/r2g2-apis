# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ai/rag/v0/stores.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61i/rag/v0/stores.proto\x12\tai.rag.v0\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd9\x04\n\tIndexFile\x12\x19\n\x08store_id\x18\x01 \x01(\tR\x07storeId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12;\n\x0bupload_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nuploadTime\x12K\n\x0e\x64irectory_info\x18\x04 \x01(\x0b\x32\".ai.rag.v0.IndexFile.DirectoryInfoH\x00R\rdirectoryInfo\x12<\n\tfile_info\x18\x05 \x01(\x0b\x32\x1d.ai.rag.v0.IndexFile.FileInfoH\x00R\x08\x66ileInfo\x1a\x92\x01\n\rDirectoryInfo\x12\x46\n\x06states\x18\x01 \x03(\x0b\x32..ai.rag.v0.IndexFile.DirectoryInfo.StatesEntryR\x06states\x1a\x39\n\x0bStatesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\rR\x05value:\x02\x38\x01\x1aq\n\x08\x46ileInfo\x12\x10\n\x03md5\x18\x01 \x01(\tR\x03md5\x12\x30\n\x05state\x18\x02 \x01(\x0e\x32\x1a.ai.rag.v0.IndexFile.StateR\x05state\x12!\n\x0cstate_reason\x18\x03 \x01(\tR\x0bstateReason\"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08INDEXING\x10\x01\x12\x0b\n\x07INDEXED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x42\x06\n\x04info\"\xaa\x01\n\x15ListIndexFilesRequest\x12\x19\n\x08store_id\x18\x01 \x01(\tR\x07storeId\x12\x1c\n\tdirectory\x18\x02 \x01(\tR\tdirectory\x12\x1c\n\trecursive\x18\x03 \x01(\x08R\trecursive\x12\x1b\n\tpage_size\x18\x05 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x06 \x01(\tR\tpageToken\"l\n\x16ListIndexFilesResponse\x12*\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x14.ai.rag.v0.IndexFileR\x05\x66iles\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken2a\n\x06Stores\x12W\n\x0eListIndexFiles\x12 .ai.rag.v0.ListIndexFilesRequest\x1a!.ai.rag.v0.ListIndexFilesResponse\"\x00\x42\x39Z7github.com/peak6-sites/r2g2-apis/gen/go/ai/rag/v0;ragpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ai.rag.v0.stores_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/peak6-sites/r2g2-apis/gen/go/ai/rag/v0;ragpb'
  _globals['_INDEXFILE_DIRECTORYINFO_STATESENTRY']._options = None
  _globals['_INDEXFILE_DIRECTORYINFO_STATESENTRY']._serialized_options = b'8\001'
  _globals['_INDEXFILE']._serialized_start=71
  _globals['_INDEXFILE']._serialized_end=672
  _globals['_INDEXFILE_DIRECTORYINFO']._serialized_start=332
  _globals['_INDEXFILE_DIRECTORYINFO']._serialized_end=478
  _globals['_INDEXFILE_DIRECTORYINFO_STATESENTRY']._serialized_start=421
  _globals['_INDEXFILE_DIRECTORYINFO_STATESENTRY']._serialized_end=478
  _globals['_INDEXFILE_FILEINFO']._serialized_start=480
  _globals['_INDEXFILE_FILEINFO']._serialized_end=593
  _globals['_INDEXFILE_STATE']._serialized_start=595
  _globals['_INDEXFILE_STATE']._serialized_end=664
  _globals['_LISTINDEXFILESREQUEST']._serialized_start=675
  _globals['_LISTINDEXFILESREQUEST']._serialized_end=845
  _globals['_LISTINDEXFILESRESPONSE']._serialized_start=847
  _globals['_LISTINDEXFILESRESPONSE']._serialized_end=955
  _globals['_STORES']._serialized_start=957
  _globals['_STORES']._serialized_end=1054
# @@protoc_insertion_point(module_scope)
