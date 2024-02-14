from datetime import date, time

from pydantic import BaseModel


class User(BaseModel):
    userid: int
    name: str
    password: str
    email: str


class Babysitter(BaseModel):
    babysitterid: int
    pictureid: int
    description: str
    user_id: int
    is_available: bool


class Parent(BaseModel):
    parentid: int
    description: str
    user_id: int
    emergency_contact: str


class Children(BaseModel):
    childid: int
    name: str
    birthdate: date


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


class BabysitterSkill(BaseModel):
    babysitterid: int
    skillid: int
    skillrank: int


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
