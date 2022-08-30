from typing import List
import datetime as _dt
import pydantic as _pydantic


class Token(_pydantic.BaseModel):
    id: str
    token: str
    user_id: int
    exp: _dt.datetime

    class Config:
        orm_mode = True


class User(_pydantic.BaseModel):
    id: int
    public_id: str
    name: str
    email: str
    password: str

    token: List[Token] = []

    class Config:
        orm_mode = True
