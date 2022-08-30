import os


DATABASE = {
    "user": os.environ.get("user", "user"),
    "password": os.environ.get("password", "password"),
    "db": os.environ.get("db", "db"),
    "host": os.environ.get("host", "database")
}

TOKEN_LIFE_TIME = 120
AUTH_HOST = "127.0.0.1:50052"