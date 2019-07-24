# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: evtmanager.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='evtmanager.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x65vtmanager.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa8\x01\n\x06\x65vtMgr\x12\n\n\x02id\x18\x01 \x01(\x03\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x0b\n\x03src\x18\x04 \x01(\t\x12\x0b\n\x03\x63\x61t\x18\x05 \x01(\x05\x12\x10\n\x08\x64\x61taList\x18\x06 \x03(\t\x12\x10\n\x08hostname\x18\x07 \x01(\t\x12\x10\n\x08username\x18\x08 \x01(\t\x12\n\n\x02os\x18\t \x01(\t\"\x18\n\x03\x61\x63k\x12\x11\n\tisDeliver\x18\x01 \x01(\x08\x32$\n\x06Pusher\x12\x1a\n\x07PushLog\x12\x07.evtMgr\x1a\x04.ack\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_EVTMGR = _descriptor.Descriptor(
  name='evtMgr',
  full_name='evtMgr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='evtMgr.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='evtMgr.time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='evtMgr.type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src', full_name='evtMgr.src', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cat', full_name='evtMgr.cat', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataList', full_name='evtMgr.dataList', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='evtMgr.hostname', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='evtMgr.username', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os', full_name='evtMgr.os', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=222,
)


_ACK = _descriptor.Descriptor(
  name='ack',
  full_name='ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isDeliver', full_name='ack.isDeliver', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=248,
)

_EVTMGR.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['evtMgr'] = _EVTMGR
DESCRIPTOR.message_types_by_name['ack'] = _ACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

evtMgr = _reflection.GeneratedProtocolMessageType('evtMgr', (_message.Message,), {
  'DESCRIPTOR' : _EVTMGR,
  '__module__' : 'evtmanager_pb2'
  # @@protoc_insertion_point(class_scope:evtMgr)
  })
_sym_db.RegisterMessage(evtMgr)

ack = _reflection.GeneratedProtocolMessageType('ack', (_message.Message,), {
  'DESCRIPTOR' : _ACK,
  '__module__' : 'evtmanager_pb2'
  # @@protoc_insertion_point(class_scope:ack)
  })
_sym_db.RegisterMessage(ack)



_PUSHER = _descriptor.ServiceDescriptor(
  name='Pusher',
  full_name='Pusher',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=250,
  serialized_end=286,
  methods=[
  _descriptor.MethodDescriptor(
    name='PushLog',
    full_name='Pusher.PushLog',
    index=0,
    containing_service=None,
    input_type=_EVTMGR,
    output_type=_ACK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PUSHER)

DESCRIPTOR.services_by_name['Pusher'] = _PUSHER

# @@protoc_insertion_point(module_scope)
