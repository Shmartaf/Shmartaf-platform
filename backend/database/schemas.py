from datetime import date, time
from typing import Optional
from uuid import uuid4

from pydantic import UUID4, BaseModel, EmailStr


class RequirementsIdSchema(BaseModel):
    id: Optional[UUID4] = uuid4().hex


class RequirementsSchema(RequirementsIdSchema):
    needname: str


class ChildReqirmentsRequestSchema(BaseModel):
    childid: UUID4
    needrank: int
    needid: UUID4


class ChildrenRequirementsSchema(ChildReqirmentsRequestSchema):
    need_skills: Optional[RequirementsSchema] = None


class CertificationSchema(BaseModel):
    id: Optional[UUID4] = uuid4().hex
    skillname: str
    skill_needs: Optional[list[Optional[RequirementsSchema]]] = []


class BabysitterCerticationRequestSchema(BaseModel):
    babysitterid: UUID4
    skillrank: int
    id: UUID4


class BabysitterCertificationSchema(BabysitterCerticationRequestSchema):
    skill: Optional[CertificationSchema] = None


class UserIdSchema(BaseModel):
    id: Optional[UUID4] = uuid4().hex


class UserSchema(UserIdSchema):
    name: str
    password: str
    email: EmailStr
    phone: str
    registrationdate: date
    city: str
    street: str


class ContactedRequestSchema(BaseModel):
    id: Optional[UUID4] = uuid4().hex
    parentid: UUID4
    babysitterid: UUID4
    date: date


class BabysitterRequestSchema(BaseModel):
    id: Optional[UUID4] = uuid4().hex
    pictureid: int
    description: str


class ScheduleSchema(BabysitterRequestSchema):
    date: date
    starttime: time
    endtime: time


class BabysitterSchema(BabysitterRequestSchema):
    user: UserSchema
    skills: Optional[list[BabysitterCertificationSchema]] = []
    contacted_babysitters: Optional[list[ContactedRequestSchema]] = []
    schedules: Optional[list[ScheduleSchema]] = []


BabysitterSchema.update_forward_refs()


class ChildrenResponseRequirementsSchema(ChildrenRequirementsSchema):
    need: Optional[RequirementsSchema] = None


class ChildrenRequestSchema(BaseModel):
    id: Optional[UUID4] = uuid4().hex
    name: str
    birthdate: date
    gender: str


class ChildrenSchema(ChildrenRequestSchema):
    needs: Optional[list[ChildrenResponseRequirementsSchema]] = []


class ReviewSchema(BaseModel):
    id: Optional[UUID4] = uuid4().hex
    reviewerid: UUID4
    reviewedid: UUID4
    rating: int
    comment: str
    flexibilityrating: int
    reliabilityrating: int
    interpersonalrating: int
    registrationdate: date


class ParentSchema(BaseModel):
    id: Optional[UUID4] = uuid4().hex
    description: str


class ContactedSchema(ContactedRequestSchema):
    parent: Optional[ParentSchema]
    babysitter: Optional[BabysitterSchema]
    id: Optional[UUID4] = uuid4().hex
    date: date


class FavoriteRequestSchema(BaseModel):
    parentid: UUID4
    babysitterid: UUID4


class FavoriteSchema(BaseModel):
    parent: Optional[ParentSchema]
    babysitter: Optional[BabysitterSchema]


class ParentResponseSchema(ParentSchema):
    user: UserSchema
    childrens: Optional[list[Optional[ChildrenSchema]]]
    contacted: list[Optional[ContactedSchema]]
    favorites: Optional[list[Optional[FavoriteSchema]]]


class ParentChildrenRequestSchema(BaseModel):
    parentid: UUID4
    childid: UUID4


class RequirementsCertificationScheme(BaseModel):
    needid: UUID4
    skillid: UUID4
