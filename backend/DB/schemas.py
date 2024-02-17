from datetime import date, time
from typing import Optional

from pydantic import BaseModel


class SpecialNeed(BaseModel):
    needid: int
    needname: str


class SpecialSkillRead(BaseModel):
    skillid: int
    skillname: str


class NeedSkill(SpecialNeed, SpecialSkillRead):
    needid: int
    skillid: int
    skill_needs: Optional[list[SpecialNeed]] = None
    # skill: SpecialSkill


class User(BaseModel):
    userid: int
    name: str
    # password: str
    email: str


class BabysitterSkillRead(BaseModel):
    skill: SpecialSkillRead
    skillrank: int


class Babysitter(BaseModel):
    babysitterid: int
    pictureid: int
    description: str
    skills: list[BabysitterSkillRead]


class BabysitterRead(Babysitter):
    user: Optional[User] = None
    skills: Optional[list[BabysitterSkillRead]] = None


class ChildrensNeedsRead(BaseModel):
    need: SpecialNeed
    needrank: int


class Children(BaseModel):
    childid: int
    name: str
    birthdate: date
    needs_association: Optional[list[ChildrensNeedsRead]] = None


class ChildrenRead(Children):
    needs_association: Optional[list[ChildrensNeedsRead]] = None


class Parent(BaseModel):
    parentid: int
    description: str


class ParentRead(Parent):
    user: Optional[User] = None
    children: Optional[list[ChildrenRead]] = None


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
