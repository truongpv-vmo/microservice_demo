import redis

from settings import *


pool = redis.ConnectionPool(
    host=REDIS_HOST,
    port=REDIS_PORT, 
    password=REDIS_PASSWORD)

r = redis.Redis(connection_pool=pool)


def update_cart():
    pass


def update_cart():
    pass

class CacheManagement():
    def __init__(self) -> None:
        pass

    def buid_key(self, ):
        pass
