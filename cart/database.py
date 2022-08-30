import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from settings import *

SQLALCHEMY_DATABASE_URL = f'mysql://{DATABASE["user"]}:{DATABASE["password"]}@{DATABASE["host"]}/{DATABASE["db"]}'

engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()