import grpc
import pdb

import profileService_pb2 as ps
import profileService_pb2_grpc as ps_grpc

import fake_help


# 
# constants
#

SEASON = 'Spring'
YEAR = 2018


class ProfileServiceClient():

    def __init__(self, channel='localhost:50051'):
        channel = grpc.insecure_channel(channel)
        self.stub = ps_grpc.ProfileServiceStub(channel)

    def create_user_profile(self, first_name, last_name, profile):
        proto_term = ps.Term(season=SEASON, year=YEAR)

        proto_user = ps.User(firstName=first_name, lastName=last_name, 
                term=proto_term)

        proto_profile = ps.Profile(profile=profile)

        create_user_profile_request = ps.CreateUserProfileRequest(
                user = proto_user,
                profile = proto_profile
        )

        response = self.stub.CreateUserProfile(
                create_user_profile_request
        )
        
        return response


if __name__ == '__main__':
    client = ProfileServiceClient()

    first, last = fake_help.generate_names(1).pop()
    profile = fake_help.make_profile()
    print(client.create_user_profile(first, last, profile))
