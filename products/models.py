from peewee import *
import datetime, os
from datetime import timedelta, datetime
from playhouse.db_url import connect

DATABASE = {
    "user": os.environ.get("user", "root"),
    "password": os.environ.get("password", "password"),
    "db": os.environ.get("db", "products"),
    "host": os.environ.get("host", "mysql")
}

TOKEN_LIFE_TIME = 120
db = connect(f'mysql://{DATABASE["user"]}:{DATABASE["password"]}@{DATABASE["host"]}/{DATABASE["db"]}')


class PriceUnit(Model):
    class Meta:
        database = db

    id = IntegerField(primary_key=True)
    currencyCode = CharField()


class Products(Model):
    class Meta:
        database = db

    id = IntegerField(primary_key=True)
    name = CharField()
    description = TextField()
    picture = TextField()
    total = IntegerField()
    unit = ForeignKeyField(PriceUnit)
    categories = TextField()

