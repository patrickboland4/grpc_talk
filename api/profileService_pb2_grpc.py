# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import profileService_pb2 as profileService__pb2


class ProfileServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateUserProfile = channel.unary_unary(
        '/grpcTalk.ProfileService/CreateUserProfile',
        request_serializer=profileService__pb2.CreateUserProfileRequest.SerializeToString,
        response_deserializer=profileService__pb2.CreateUserProfileResponse.FromString,
        )
    self.GetUserProfile = channel.unary_unary(
        '/grpcTalk.ProfileService/GetUserProfile',
        request_serializer=profileService__pb2.GetUserProfileRequest.SerializeToString,
        response_deserializer=profileService__pb2.GetUserProfileResponse.FromString,
        )


class ProfileServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateUserProfile(self, request, context):
    """Create a profile
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUserProfile(self, request, context):
    """Get the mentee or mentor details 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProfileServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateUserProfile': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUserProfile,
          request_deserializer=profileService__pb2.CreateUserProfileRequest.FromString,
          response_serializer=profileService__pb2.CreateUserProfileResponse.SerializeToString,
      ),
      'GetUserProfile': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserProfile,
          request_deserializer=profileService__pb2.GetUserProfileRequest.FromString,
          response_serializer=profileService__pb2.GetUserProfileResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpcTalk.ProfileService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))