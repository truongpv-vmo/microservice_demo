import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import database as _database


class User(_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    public_id = _sql.Column(_sql.String)
    email = _sql.Column(_sql.String, unique=True, index=True)
    password = _sql.Column(_sql.String)
    token = _orm.relationship("Token", back_populates="user")


class Token(_database.Base):
    __tablename__ = "token"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    token = _sql.Column(_sql.String, index=True)
    user_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    exp = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    owner = _orm.relationship("User", back_populates="Token")
