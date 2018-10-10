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

    
    def create_user_profiles(self, first_last_profile_tuple_list):
        create_user_profiles_request = ps.CreateUserProfilesRequest(
                user_profiles = [ps.CreateUserProfileRequest(
                    user=ps.User(firstName=item[0][0], lastName=item[0][1],
                        term=ps.Term(season=SEASON, year=YEAR)),
                    profile=ps.Profile(profile=item[1]))
                    for item in first_last_profile_tuple_list
                ]
        )

        responses = self.stub.CreateUserProfiles(create_user_profiles_request)

        responses = [response for response in responses]

        return responses



        



if __name__ == '__main__':
    client = ProfileServiceClient()

    #first, last = fake_help.generate_names(1).pop()
    #profile = fake_help.make_profile()

    #print(client.create_user_profile(first, last, profile))

    num = 2
    name_list = fake_help.generate_names(num)
    profile_list = [fake_help.make_profile() for _ in range(num)]
    name_profile_list = list(zip(name_list, profile_list))
    print(client.create_user_profiles(name_profile_list))




