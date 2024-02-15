from datetime import date, time
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    userid: int
    name: str
    # password: str
    email: str


class BabysitterSkill(BaseModel):
    babysitterid: int
    skillid: int
    skillrank: int


class Babysitter(BaseModel):
    babysitterid: int
    pictureid: int
    description: str
    # skills: list[BabysitterSkill]


class BabysitterRead(Babysitter):
    user: Optional[User] = None


class Parent(BaseModel):
    parentid: int
    description: str
    # # add user derived from user table
    # name: str
    # password: str
    # email: str
    # registrationdate: date
    # city: str
    # street: str
    # phone: str


class ParentRead(Parent):
    user: Optional[User] = None


class Children(BaseModel):
    childid: int
    name: str
    birthdate: date


class ChildrenRead(Children):
    parents: Optional[list[Parent]] = None


class ParentsChildrens(BaseModel):
    childid: int
    parentid: int


class Review(BaseModel):
    reviewid: int
    reviewerid: int
    reviewedid: int
    rating: float
    flexibilityrating: float
    reliabilityrating: float
    interpersonalrating: float
    comment: str
    publicationdate: date
    review_text: str


class SpecialNeed(BaseModel):
    specialneedid: int
    name: str


class SpecialSkill(BaseModel):
    specialskillid: int
    name: str


class NeedSkill(BaseModel):
    needid: int
    skillid: int


class Favorite(BaseModel):
    parentid: int
    babysitterid: int


class Contacted(BaseModel):
    parentid: int
    babysitterid: int
    date: date


class Scheduler(BaseModel):
    babysitterid: int
    starttime: time
    endtime: time
    dayinweek: str
