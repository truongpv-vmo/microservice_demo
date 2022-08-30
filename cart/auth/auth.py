import grpc

from . import auth_pb2
from . import auth_pb2_grpc
from settings import AUTH_HOST


def valid_token(token):
    channel = grpc.insecure_channel(AUTH_HOST)
    stub = auth_pb2_grpc.AuthControllerStub(channel)
    response = stub.CheckToken(auth_pb2.Auth(access_token=token))
    if response.user_id:
        return True, response
    return False, None
