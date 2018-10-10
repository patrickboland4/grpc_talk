# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profileService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='profileService.proto',
  package='grpcTalk',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14profileService.proto\x12\x08grpcTalk\"I\n\x04User\x12\x11\n\tfirstName\x18\x01 \x01(\t\x12\x10\n\x08lastName\x18\x02 \x01(\t\x12\x1c\n\x04term\x18\x03 \x01(\x0b\x32\x0e.grpcTalk.Term\"$\n\x04Term\x12\x0e\n\x06season\x18\x01 \x01(\t\x12\x0c\n\x04year\x18\x02 \x01(\x05\"\x1a\n\x07Profile\x12\x0f\n\x07profile\x18\x01 \x01(\t\"\\\n\x18\x43reateUserProfileRequest\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.grpcTalk.User\x12\"\n\x07profile\x18\x02 \x01(\x0b\x32\x11.grpcTalk.Profile\"+\n\x19\x43reateUserProfileResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"V\n\x19\x43reateUserProfilesRequest\x12\x39\n\ruser_profiles\x18\x01 \x03(\x0b\x32\".grpcTalk.CreateUserProfileRequest\"S\n\x1a\x43reateUserProfilesResponse\x12\x35\n\x08statuses\x18\x01 \x03(\x0b\x32#.grpcTalk.CreateUserProfileResponse\"5\n\x15GetUserProfileRequest\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.grpcTalk.User\"Z\n\x16GetUserProfileResponse\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.grpcTalk.User\x12\"\n\x07profile\x18\x02 \x01(\x0b\x32\x11.grpcTalk.Profile\",\n\x15GetAllProfilesRequest\x12\x13\n\x0bnumProfiles\x18\x01 \x01(\x05\"L\n\x16GetAllProfilesResponse\x12\x32\n\x08profiles\x18\x01 \x03(\x0b\x32 .grpcTalk.GetUserProfileResponse2\xff\x02\n\x0eProfileService\x12\\\n\x11\x43reateUserProfile\x12\".grpcTalk.CreateUserProfileRequest\x1a#.grpcTalk.CreateUserProfileResponse\x12\x63\n\x12\x43reateUserProfiles\x12#.grpcTalk.CreateUserProfilesRequest\x1a$.grpcTalk.CreateUserProfilesResponse(\x01\x30\x01\x12S\n\x0eGetUserProfile\x12\x1f.grpcTalk.GetUserProfileRequest\x1a .grpcTalk.GetUserProfileResponse\x12U\n\x0eGetAllProfiles\x12\x1f.grpcTalk.GetAllProfilesRequest\x1a .grpcTalk.GetAllProfilesResponse0\x01\x62\x06proto3')
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='grpcTalk.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firstName', full_name='grpcTalk.User.firstName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastName', full_name='grpcTalk.User.lastName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='term', full_name='grpcTalk.User.term', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=34,
  serialized_end=107,
)


_TERM = _descriptor.Descriptor(
  name='Term',
  full_name='grpcTalk.Term',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='season', full_name='grpcTalk.Term.season', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='grpcTalk.Term.year', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=109,
  serialized_end=145,
)


_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='grpcTalk.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profile', full_name='grpcTalk.Profile.profile', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=147,
  serialized_end=173,
)


_CREATEUSERPROFILEREQUEST = _descriptor.Descriptor(
  name='CreateUserProfileRequest',
  full_name='grpcTalk.CreateUserProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='grpcTalk.CreateUserProfileRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='grpcTalk.CreateUserProfileRequest.profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=175,
  serialized_end=267,
)


_CREATEUSERPROFILERESPONSE = _descriptor.Descriptor(
  name='CreateUserProfileResponse',
  full_name='grpcTalk.CreateUserProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='grpcTalk.CreateUserProfileResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=269,
  serialized_end=312,
)


_CREATEUSERPROFILESREQUEST = _descriptor.Descriptor(
  name='CreateUserProfilesRequest',
  full_name='grpcTalk.CreateUserProfilesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_profiles', full_name='grpcTalk.CreateUserProfilesRequest.user_profiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=314,
  serialized_end=400,
)


_CREATEUSERPROFILESRESPONSE = _descriptor.Descriptor(
  name='CreateUserProfilesResponse',
  full_name='grpcTalk.CreateUserProfilesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statuses', full_name='grpcTalk.CreateUserProfilesResponse.statuses', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=402,
  serialized_end=485,
)


_GETUSERPROFILEREQUEST = _descriptor.Descriptor(
  name='GetUserProfileRequest',
  full_name='grpcTalk.GetUserProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='grpcTalk.GetUserProfileRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=487,
  serialized_end=540,
)


_GETUSERPROFILERESPONSE = _descriptor.Descriptor(
  name='GetUserProfileResponse',
  full_name='grpcTalk.GetUserProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='grpcTalk.GetUserProfileResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='grpcTalk.GetUserProfileResponse.profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=542,
  serialized_end=632,
)


_GETALLPROFILESREQUEST = _descriptor.Descriptor(
  name='GetAllProfilesRequest',
  full_name='grpcTalk.GetAllProfilesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numProfiles', full_name='grpcTalk.GetAllProfilesRequest.numProfiles', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=634,
  serialized_end=678,
)


_GETALLPROFILESRESPONSE = _descriptor.Descriptor(
  name='GetAllProfilesResponse',
  full_name='grpcTalk.GetAllProfilesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profiles', full_name='grpcTalk.GetAllProfilesResponse.profiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=680,
  serialized_end=756,
)

_USER.fields_by_name['term'].message_type = _TERM
_CREATEUSERPROFILEREQUEST.fields_by_name['user'].message_type = _USER
_CREATEUSERPROFILEREQUEST.fields_by_name['profile'].message_type = _PROFILE
_CREATEUSERPROFILESREQUEST.fields_by_name['user_profiles'].message_type = _CREATEUSERPROFILEREQUEST
_CREATEUSERPROFILESRESPONSE.fields_by_name['statuses'].message_type = _CREATEUSERPROFILERESPONSE
_GETUSERPROFILEREQUEST.fields_by_name['user'].message_type = _USER
_GETUSERPROFILERESPONSE.fields_by_name['user'].message_type = _USER
_GETUSERPROFILERESPONSE.fields_by_name['profile'].message_type = _PROFILE
_GETALLPROFILESRESPONSE.fields_by_name['profiles'].message_type = _GETUSERPROFILERESPONSE
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Term'] = _TERM
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['CreateUserProfileRequest'] = _CREATEUSERPROFILEREQUEST
DESCRIPTOR.message_types_by_name['CreateUserProfileResponse'] = _CREATEUSERPROFILERESPONSE
DESCRIPTOR.message_types_by_name['CreateUserProfilesRequest'] = _CREATEUSERPROFILESREQUEST
DESCRIPTOR.message_types_by_name['CreateUserProfilesResponse'] = _CREATEUSERPROFILESRESPONSE
DESCRIPTOR.message_types_by_name['GetUserProfileRequest'] = _GETUSERPROFILEREQUEST
DESCRIPTOR.message_types_by_name['GetUserProfileResponse'] = _GETUSERPROFILERESPONSE
DESCRIPTOR.message_types_by_name['GetAllProfilesRequest'] = _GETALLPROFILESREQUEST
DESCRIPTOR.message_types_by_name['GetAllProfilesResponse'] = _GETALLPROFILESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.User)
  ))
_sym_db.RegisterMessage(User)

Term = _reflection.GeneratedProtocolMessageType('Term', (_message.Message,), dict(
  DESCRIPTOR = _TERM,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.Term)
  ))
_sym_db.RegisterMessage(Term)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), dict(
  DESCRIPTOR = _PROFILE,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.Profile)
  ))
_sym_db.RegisterMessage(Profile)

CreateUserProfileRequest = _reflection.GeneratedProtocolMessageType('CreateUserProfileRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUSERPROFILEREQUEST,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.CreateUserProfileRequest)
  ))
_sym_db.RegisterMessage(CreateUserProfileRequest)

CreateUserProfileResponse = _reflection.GeneratedProtocolMessageType('CreateUserProfileResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUSERPROFILERESPONSE,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.CreateUserProfileResponse)
  ))
_sym_db.RegisterMessage(CreateUserProfileResponse)

CreateUserProfilesRequest = _reflection.GeneratedProtocolMessageType('CreateUserProfilesRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUSERPROFILESREQUEST,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.CreateUserProfilesRequest)
  ))
_sym_db.RegisterMessage(CreateUserProfilesRequest)

CreateUserProfilesResponse = _reflection.GeneratedProtocolMessageType('CreateUserProfilesResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUSERPROFILESRESPONSE,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.CreateUserProfilesResponse)
  ))
_sym_db.RegisterMessage(CreateUserProfilesResponse)

GetUserProfileRequest = _reflection.GeneratedProtocolMessageType('GetUserProfileRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERPROFILEREQUEST,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.GetUserProfileRequest)
  ))
_sym_db.RegisterMessage(GetUserProfileRequest)

GetUserProfileResponse = _reflection.GeneratedProtocolMessageType('GetUserProfileResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERPROFILERESPONSE,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.GetUserProfileResponse)
  ))
_sym_db.RegisterMessage(GetUserProfileResponse)

GetAllProfilesRequest = _reflection.GeneratedProtocolMessageType('GetAllProfilesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETALLPROFILESREQUEST,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.GetAllProfilesRequest)
  ))
_sym_db.RegisterMessage(GetAllProfilesRequest)

GetAllProfilesResponse = _reflection.GeneratedProtocolMessageType('GetAllProfilesResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETALLPROFILESRESPONSE,
  __module__ = 'profileService_pb2'
  # @@protoc_insertion_point(class_scope:grpcTalk.GetAllProfilesResponse)
  ))
_sym_db.RegisterMessage(GetAllProfilesResponse)



_PROFILESERVICE = _descriptor.ServiceDescriptor(
  name='ProfileService',
  full_name='grpcTalk.ProfileService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=759,
  serialized_end=1142,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUserProfile',
    full_name='grpcTalk.ProfileService.CreateUserProfile',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERPROFILEREQUEST,
    output_type=_CREATEUSERPROFILERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateUserProfiles',
    full_name='grpcTalk.ProfileService.CreateUserProfiles',
    index=1,
    containing_service=None,
    input_type=_CREATEUSERPROFILESREQUEST,
    output_type=_CREATEUSERPROFILESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserProfile',
    full_name='grpcTalk.ProfileService.GetUserProfile',
    index=2,
    containing_service=None,
    input_type=_GETUSERPROFILEREQUEST,
    output_type=_GETUSERPROFILERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllProfiles',
    full_name='grpcTalk.ProfileService.GetAllProfiles',
    index=3,
    containing_service=None,
    input_type=_GETALLPROFILESREQUEST,
    output_type=_GETALLPROFILESRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROFILESERVICE)

DESCRIPTOR.services_by_name['ProfileService'] = _PROFILESERVICE

# @@protoc_insertion_point(module_scope)
