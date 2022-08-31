# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproduct.proto\x12\x08products\">\n\x05Param\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncategories\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"(\n\x04unit\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x14\n\x0c\x63urrencyCode\x18\x02 \x01(\t\"$\n\x08\x43\x61tegory\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1e\n\x0e\x43\x61tegoryString\x12\x0c\n\x04name\x18\x01 \x01(\t\"s\n\x07Product\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07picture\x18\x04 \x01(\t\x12\r\n\x05total\x18\x05 \x01(\x03\x12\x0f\n\x07unit_id\x18\x06 \x01(\x03\x12\x14\n\x0c\x63\x61tegory_ids\x18\x07 \x03(\x03\"\x17\n\tProductID\x12\n\n\x02id\x18\x01 \x01(\x03\"\xa4\x01\n\rProductDetail\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07picture\x18\x04 \x01(\t\x12\r\n\x05total\x18\x05 \x01(\x03\x12\x1c\n\x04unit\x18\x06 \x01(\x0b\x32\x0e.products.unit\x12&\n\ncategories\x18\x07 \x03(\x0b\x32\x12.products.Category\"9\n\x0cProductsList\x12)\n\x08products\x18\x01 \x03(\x0b\x32\x17.products.ProductDetail2\x8c\x02\n\x11ProductController\x12\x38\n\x0bGetProducts\x12\x0f.products.Param\x1a\x16.products.ProductsList\"\x00\x12\x42\n\x10GetProductDetail\x12\x13.products.ProductID\x1a\x17.products.ProductDetail\"\x00\x12:\n\nAddProduct\x12\x11.products.Product\x1a\x17.products.ProductDetail\"\x00\x12=\n\x0b\x41\x64\x64\x43\x61tegory\x12\x18.products.CategoryString\x1a\x12.products.Category\"\x00\x62\x06proto3')



_PARAM = DESCRIPTOR.message_types_by_name['Param']
_UNIT = DESCRIPTOR.message_types_by_name['unit']
_CATEGORY = DESCRIPTOR.message_types_by_name['Category']
_CATEGORYSTRING = DESCRIPTOR.message_types_by_name['CategoryString']
_PRODUCT = DESCRIPTOR.message_types_by_name['Product']
_PRODUCTID = DESCRIPTOR.message_types_by_name['ProductID']
_PRODUCTDETAIL = DESCRIPTOR.message_types_by_name['ProductDetail']
_PRODUCTSLIST = DESCRIPTOR.message_types_by_name['ProductsList']
Param = _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), {
  'DESCRIPTOR' : _PARAM,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:products.Param)
  })
_sym_db.RegisterMessage(Param)

unit = _reflection.GeneratedProtocolMessageType('unit', (_message.Message,), {
  'DESCRIPTOR' : _UNIT,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:products.unit)
  })
_sym_db.RegisterMessage(unit)

Category = _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORY,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:products.Category)
  })
_sym_db.RegisterMessage(Category)

CategoryString = _reflection.GeneratedProtocolMessageType('CategoryString', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYSTRING,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:products.CategoryString)
  })
_sym_db.RegisterMessage(CategoryString)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:products.Product)
  })
_sym_db.RegisterMessage(Product)

ProductID = _reflection.GeneratedProtocolMessageType('ProductID', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTID,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:products.ProductID)
  })
_sym_db.RegisterMessage(ProductID)

ProductDetail = _reflection.GeneratedProtocolMessageType('ProductDetail', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTDETAIL,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:products.ProductDetail)
  })
_sym_db.RegisterMessage(ProductDetail)

ProductsList = _reflection.GeneratedProtocolMessageType('ProductsList', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTSLIST,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:products.ProductsList)
  })
_sym_db.RegisterMessage(ProductsList)

_PRODUCTCONTROLLER = DESCRIPTOR.services_by_name['ProductController']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PARAM._serialized_start=27
  _PARAM._serialized_end=89
  _UNIT._serialized_start=91
  _UNIT._serialized_end=131
  _CATEGORY._serialized_start=133
  _CATEGORY._serialized_end=169
  _CATEGORYSTRING._serialized_start=171
  _CATEGORYSTRING._serialized_end=201
  _PRODUCT._serialized_start=203
  _PRODUCT._serialized_end=318
  _PRODUCTID._serialized_start=320
  _PRODUCTID._serialized_end=343
  _PRODUCTDETAIL._serialized_start=346
  _PRODUCTDETAIL._serialized_end=510
  _PRODUCTSLIST._serialized_start=512
  _PRODUCTSLIST._serialized_end=569
  _PRODUCTCONTROLLER._serialized_start=572
  _PRODUCTCONTROLLER._serialized_end=840
# @@protoc_insertion_point(module_scope)
