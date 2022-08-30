# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import auth_pb2 as auth__pb2


class AuthControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddToken = channel.unary_unary(
                '/auth.AuthController/AddToken',
                request_serializer=auth__pb2.UserToken.SerializeToString,
                response_deserializer=auth__pb2.User.FromString,
                )
        self.CheckToken = channel.unary_unary(
                '/auth.AuthController/CheckToken',
                request_serializer=auth__pb2.Auth.SerializeToString,
                response_deserializer=auth__pb2.User.FromString,
                )


class AuthControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddToken': grpc.unary_unary_rpc_method_handler(
                    servicer.AddToken,
                    request_deserializer=auth__pb2.UserToken.FromString,
                    response_serializer=auth__pb2.User.SerializeToString,
            ),
            'CheckToken': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckToken,
                    request_deserializer=auth__pb2.Auth.FromString,
                    response_serializer=auth__pb2.User.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.AuthController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.AuthController/AddToken',
            auth__pb2.UserToken.SerializeToString,
            auth__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.AuthController/CheckToken',
            auth__pb2.Auth.SerializeToString,
            auth__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)