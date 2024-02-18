from datetime import date, time
from typing import Optional, Union

from pydantic import BaseModel

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

class SpecialNeed(BaseModel):
    id: int
    needname: str


class SpecialSkillRead(BaseModel):
    id: int
    skillname: str


class NeedSkill(SpecialNeed, SpecialSkillRead):
    needid: int
    skillid: int
    skill_needs: Optional[list[SpecialNeed]] = None
    # skill: SpecialSkill

class User(BaseModel):
    id: int  # Add the id field
    name: str 
    password: str
    email: str
    phone: str
    registrationdate: date
    city: str
    street: str

class BabysitterSkillRead(BaseModel):
    skill: SpecialSkillRead
    skillrank: int


class Babysitter(BaseModel):
    id: int
    pictureid: int
    description: str
    # skills: list[BabysitterSkillRead]


class BabysitterRead(Babysitter):
    user: Optional[User] = None
    skills: Optional[list[BabysitterSkillRead]] = None
    schedules: Optional[list[Scheduler]] = None
    contacted_babysitters: Optional[list[Contacted]] = None


class ChildrensNeedsRead(BaseModel):
    need: SpecialNeed
    needrank: int


class Children(BaseModel):
    id: int
    name: str
    birthdate: date


class ChildrenRead(Children):
    needs_association: Optional[list[ChildrensNeedsRead]] = None


class Parent(BaseModel):
    id: int
    description: str


class ParentRead(Parent):
    user: Optional[User] = None
    children: Optional[list[ChildrenRead]] = None
    favorites: Optional[list[Favorite]] = None
    contacted_parents: Optional[list[Contacted]] = None


class ParentsChildrens(BaseModel):
    childid: int
    parentid: int


class Review(BaseModel):
    id: int
    reviewerid: int
    reviewedid: int
    rating: float
    flexibilityrating: float
    reliabilityrating: float
    interpersonalrating: float
    comment: str
    registrationdate: date

class ReviewRead(BaseModel):
    pass
    id: int
    reviewerid: int
    reviewer: User
    reviewed: User
    rating: float
    flexibilityrating: float
    reliabilityrating: float
    interpersonalrating: float






