# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\"\x1c\n\x04\x41uth\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\"+\n\tUserToken\x12\r\n\x05token\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\"\x17\n\x04User\x12\x0f\n\x07user_id\x18\x02 \x01(\x03\x32\x63\n\x0e\x41uthController\x12)\n\x08\x41\x64\x64Token\x12\x0f.auth.UserToken\x1a\n.auth.User\"\x00\x12&\n\nCheckToken\x12\n.auth.Auth\x1a\n.auth.User\"\x00\x62\x06proto3')



_AUTH = DESCRIPTOR.message_types_by_name['Auth']
_USERTOKEN = DESCRIPTOR.message_types_by_name['UserToken']
_USER = DESCRIPTOR.message_types_by_name['User']
Auth = _reflection.GeneratedProtocolMessageType('Auth', (_message.Message,), {
  'DESCRIPTOR' : _AUTH,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.Auth)
  })
_sym_db.RegisterMessage(Auth)

UserToken = _reflection.GeneratedProtocolMessageType('UserToken', (_message.Message,), {
  'DESCRIPTOR' : _USERTOKEN,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.UserToken)
  })
_sym_db.RegisterMessage(UserToken)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.User)
  })
_sym_db.RegisterMessage(User)

_AUTHCONTROLLER = DESCRIPTOR.services_by_name['AuthController']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUTH._serialized_start=20
  _AUTH._serialized_end=48
  _USERTOKEN._serialized_start=50
  _USERTOKEN._serialized_end=93
  _USER._serialized_start=95
  _USER._serialized_end=118
  _AUTHCONTROLLER._serialized_start=120
  _AUTHCONTROLLER._serialized_end=219
# @@protoc_insertion_point(module_scope)
