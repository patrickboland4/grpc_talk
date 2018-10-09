from concurrent import futures
import time

import grpc

from . import profileService_pb2 as ps
from . import profileService_pb2_grpc as ps_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ProfileServicer(ps_grpc.ProfileServiceServicer):

    def CreateUser(self, request, context):
        # do stuff
        response = ps.CreateUserProfileResponse(
                status = "OK"
        )


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


