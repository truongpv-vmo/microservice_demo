import os


DATABASE = {
    "user": os.environ.get("user", "user"),
    "password": os.environ.get("password", "password"),
    "db": os.environ.get("db", "db"),
    "host": os.environ.get("host", "database")
}
