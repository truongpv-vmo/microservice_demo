import os

#redis
REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81")

#database
DATABASE={
    "user": os.environ.get("DATABASE_USER", "user"),
    "password": os.environ.get("DATABASE_PASSWORD", "password"),
    "db": os.environ.get("DATABASE_NAME", "db"),
    "host": os.environ.get("DATABASE_HOST", "database")
}
AUTH_HOST = "127.0.0.1:50052"