from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import logging
from google.protobuf.json_format import MessageToJson
import grpc
import product_pb2_grpc
import product_pb2
from models import Products


class LisProProductController(product_pb2_grpc.ProductControllerServicer):
    def GetProducts(self, request, _):
        name = request.name
        categories = request.categories
        description = request.description
        products = []
        for product in Products.select().where((Products.name == name) &(Products.categories.contains(categories)) & (Products.description.contains(description))):
            product = product_pb2.Product(
                id = product.id,
                name = product.name,
                description = product.description,
                picture = product.picture,
                total = product.total,
                unit_id = product.unit.id,
                categories = product.categories
            )
            products.append(product)
        return product_pb2.ProductsList(products=products)


def serve(address: str) -> None:
    server = grpc.server(ThreadPoolExecutor())
    product_pb2_grpc.add_ProductControllerServicer_to_server(LisProProductController(), server)
    server.add_insecure_port(address)
    server.start()
    logging.info("Server serving at %s", address)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve("[::]:50052")
