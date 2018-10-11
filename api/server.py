from concurrent import futures
import pdb
import time

import grpc

import profileService_pb2 as ps
import profileService_pb2_grpc as ps_grpc
import arango_helpers


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ProfileServicer(ps_grpc.ProfileServiceServicer):

    def __init__(self):
        self.arango_client = arango_helpers.ArangoHelper()

    def CreateUserProfile(self, request, context):
        first = request.user.firstName
        last = request.user.lastName
        season = request.user.term.season
        year = request.user.term.year
        profile = request.profile.profile

        profile_map = dict(
                first=first, last=last, term="{}{}".format(season, year),
                profile=profile
        )

        try:
            self.arango_client.create_user_profile(profile_map)
            response = ps.CreateUserProfileResponse(
                    status = "Profile Created"
            )
        except:
            response = ps.CreateUserProfileResponse(
                    status = "Failed to create profile"
            )

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ps_grpc.add_ProfileServiceServicer_to_server(ProfileServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()


