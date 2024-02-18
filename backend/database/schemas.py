from datetime import date, time
from typing import Optional, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    password: str
    email: str
    phone: str
    registrationdate: date
    city: str
    street: str
    roleid: int


class Role(BaseModel):
    id: int
    rolename: str
