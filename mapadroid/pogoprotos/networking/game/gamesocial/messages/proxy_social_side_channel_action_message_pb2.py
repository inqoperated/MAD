# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/game/gamesocial/messages/proxy_social_side_channel_action_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/game/gamesocial/messages/proxy_social_side_channel_action_message.proto',
  package='pogoprotos.networking.game.gamesocial.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n]pogoprotos/networking/game/gamesocial/messages/proxy_social_side_channel_action_message.proto\x12.pogoprotos.networking.game.gamesocial.messages\"T\n#ProxySocialSideChannelActionMessage\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\r\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x62\x06proto3'
)




_PROXYSOCIALSIDECHANNELACTIONMESSAGE = _descriptor.Descriptor(
  name='ProxySocialSideChannelActionMessage',
  full_name='pogoprotos.networking.game.gamesocial.messages.ProxySocialSideChannelActionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='pogoprotos.networking.game.gamesocial.messages.ProxySocialSideChannelActionMessage.action', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='pogoprotos.networking.game.gamesocial.messages.ProxySocialSideChannelActionMessage.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='pogoprotos.networking.game.gamesocial.messages.ProxySocialSideChannelActionMessage.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=145,
  serialized_end=229,
)

DESCRIPTOR.message_types_by_name['ProxySocialSideChannelActionMessage'] = _PROXYSOCIALSIDECHANNELACTIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProxySocialSideChannelActionMessage = _reflection.GeneratedProtocolMessageType('ProxySocialSideChannelActionMessage', (_message.Message,), {
  'DESCRIPTOR' : _PROXYSOCIALSIDECHANNELACTIONMESSAGE,
  '__module__' : 'pogoprotos.networking.game.gamesocial.messages.proxy_social_side_channel_action_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.game.gamesocial.messages.ProxySocialSideChannelActionMessage)
  })
_sym_db.RegisterMessage(ProxySocialSideChannelActionMessage)


# @@protoc_insertion_point(module_scope)