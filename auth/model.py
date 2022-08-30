from peewee import *
import datetime, os
from datetime import timedelta, datetime
from playhouse.db_url import connect

DATABASE = {
    "user": os.environ.get("user", "root"),
    "password": os.environ.get("password", "password"),
    "db": os.environ.get("db", "auth"),
    "host": os.environ.get("host", "mysql")
}

TOKEN_LIFE_TIME = 120
db = connect(f'mysql://{DATABASE["user"]}:{DATABASE["password"]}@{DATABASE["host"]}/{DATABASE["db"]}')

class Token(Model):
    class Meta:
        database = db

    user_id = IntegerField()
    token = TextField()
    exp = DateTimeField(default=datetime.now() + timedelta(minutes=TOKEN_LIFE_TIME))

    def create(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.exp = datetime.now() + timedelta(minutes=TOKEN_LIFE_TIME)
        self.save()
