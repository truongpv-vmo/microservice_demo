from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import logging
from google.protobuf.json_format import MessageToJson
import grpc
import auth_pb2_grpc
import auth_pb2
from model import Token


class Auth(auth_pb2_grpc.AuthControllerServicer):
    def CheckToken(self, request, token):
        try:
            user_id = Token.get(Token.token == request.access_token, Token.exp > datetime.now()).user_id
        except Token.DoesNotExist:
            return auth_pb2.User()
        return auth_pb2.User(user_id=user_id)


    def AddToken(self, request, token):
        print(request)
        Token().create(token = request.token, user_id=request.user_id)
        return auth_pb2.User(user_id=request.user_id)


def serve(address: str) -> None:
    server = grpc.server(ThreadPoolExecutor())
    auth_pb2_grpc.add_AuthControllerServicer_to_server(Auth(), server)
    server.add_insecure_port(address)
    server.start()
    logging.info("Server serving at %s", address)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve("[::]:50052")
