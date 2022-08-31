from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import logging
from unicodedata import category
from google.protobuf.json_format import MessageToJson
import grpc
import product_pb2_grpc
import product_pb2
from models import Products, Categories, ProductsCategories


class LisProProductController(product_pb2_grpc.ProductControllerServicer):
    def GetProducts(self, request, _):
        name = request.name
        categories = request.categories
        description = request.description
        products = []

        if categories:
            product_ids = ProductsCategories.select(ProductsCategories.product_id).join(
                Categories, on=(Categories.id == ProductsCategories.category_id)
            ).where(Categories.name.contains(categories))
        for product in Products.select().where(
                        (Products.name.contains(name)) &
                        (Products.id.in_(product_ids)) & 
                        (Products.description.contains(description))
                    ):
            categories = []
            for products_categories in ProductsCategories.select().where(ProductsCategories.product_id==product.id):
                categories.append(
                    product_pb2.Category(
                        id=products_categories.category.id,
                        name=products_categories.category.name
                    )
                )
            product = product_pb2.ProductDetail(
                id = product.id,
                name = product.name,
                description = product.description,
                picture = product.picture,
                total = product.total,
                unit = product_pb2.unit(id = product.unit.id, currencyCode= product.unit.currencyCode),
                categories = categories
            )
            products.append(product)
        return product_pb2.ProductsList(products=products)

    def GetProductDetail(self, request, _):
        try:
            product = Products.get(Products.id==request.id)
            categories = []
            for products_categories in ProductsCategories.select().where(ProductsCategories.product_id==product.id):
                categories.append(
                    product_pb2.Category(
                        id=products_categories.category.id,
                        name=products_categories.category.name
                    )
                )

            return product_pb2.ProductDetail(
                id = product.id,
                name = product.name,
                description = product.description,
                picture = product.picture,
                total = product.total,
                unit = product_pb2.unit(id = product.unit.id, currencyCode= product.unit.currencyCode),
                categories = categories
            )    
        except Products.DoesNotExist:
            return product_pb2.ProductDetail()

    def AddProduct(self, request, _):
        product = Products(
                name = request.name,
                description = request.description,
                picture = request.picture,
                total = request.total,
                unit_id = request.unit_id,
            )
        product.save()
        categories = []
        for category in request.category_ids:
            products_categories = ProductsCategories.create(
                category_id = category,
                product_id = product.id
            )
            categories.append(
                product_pb2.Category(
                    id=products_categories.category.id,
                    name=products_categories.category.name
                )
            )

        return product_pb2.ProductDetail(
                id = product.id,
                name = product.name,
                description = product.description,
                picture = product.picture,
                total = product.total,
                unit = product_pb2.unit(id = product.unit.id, currencyCode= product.unit.currencyCode),
                categories = categories
        )

    def AddCategory(self, request,_):
        category = Categories.create(
            name = request.name
        )
        return product_pb2.Category(id=category.id, name=category.name)


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
