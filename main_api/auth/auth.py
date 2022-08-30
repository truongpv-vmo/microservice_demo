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


def add_token(token, user_id):
    channel = grpc.insecure_channel(AUTH_HOST)
    stub = auth_pb2_grpc.AuthControllerStub(channel)
    response = stub.AddToken(auth_pb2.UserToken(access_token=token, user_id=user_id))
    if response.user_id:
        return True, response
    return False, None