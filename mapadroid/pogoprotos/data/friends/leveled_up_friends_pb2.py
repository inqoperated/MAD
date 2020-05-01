# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/friends/leveled_up_friends.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_public_profile_pb2 as pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2
from pogoprotos.data.friends import friendship_level_data_pb2 as pogoprotos_dot_data_dot_friends_dot_friendship__level__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/friends/leveled_up_friends.proto',
  package='pogoprotos.data.friends',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n0pogoprotos/data/friends/leveled_up_friends.proto\x12\x17pogoprotos.data.friends\x1a\x32pogoprotos/data/player/player_public_profile.proto\x1a\x33pogoprotos/data/friends/friendship_level_data.proto\"\xa7\x01\n\x10LeveledUpFriends\x12\x44\n\x0f\x66riend_profiles\x18\x01 \x03(\x0b\x32+.pogoprotos.data.player.PlayerPublicProfile\x12M\n\x17\x66riend_milestone_levels\x18\x02 \x03(\x0b\x32,.pogoprotos.data.friends.FriendshipLevelDatab\x06proto3'
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_friends_dot_friendship__level__data__pb2.DESCRIPTOR,])




_LEVELEDUPFRIENDS = _descriptor.Descriptor(
  name='LeveledUpFriends',
  full_name='pogoprotos.data.friends.LeveledUpFriends',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='friend_profiles', full_name='pogoprotos.data.friends.LeveledUpFriends.friend_profiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_milestone_levels', full_name='pogoprotos.data.friends.LeveledUpFriends.friend_milestone_levels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=183,
  serialized_end=350,
)

_LEVELEDUPFRIENDS.fields_by_name['friend_profiles'].message_type = pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2._PLAYERPUBLICPROFILE
_LEVELEDUPFRIENDS.fields_by_name['friend_milestone_levels'].message_type = pogoprotos_dot_data_dot_friends_dot_friendship__level__data__pb2._FRIENDSHIPLEVELDATA
DESCRIPTOR.message_types_by_name['LeveledUpFriends'] = _LEVELEDUPFRIENDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LeveledUpFriends = _reflection.GeneratedProtocolMessageType('LeveledUpFriends', (_message.Message,), {
  'DESCRIPTOR' : _LEVELEDUPFRIENDS,
  '__module__' : 'pogoprotos.data.friends.leveled_up_friends_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.friends.LeveledUpFriends)
  })
_sym_db.RegisterMessage(LeveledUpFriends)


# @@protoc_insertion_point(module_scope)