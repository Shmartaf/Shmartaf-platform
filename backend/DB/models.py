from database import Base
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Text, Time
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    userid = Column(Integer, primary_key=True)
    name = Column(String(255))
    gender = Column(String(10))
    email = Column(String(255))
    password = Column(String(255))
    registrationdate = Column(Date)
    city = Column(String(255))
    street = Column(String(255))
    phone = Column(String(15))
    parent = relationship("Parent", uselist=False, back_populates="user")
    babysitter = relationship("Babysitter", uselist=False, back_populates="user")


class Babysitter(Base):
    __tablename__ = "babysitter"

    babysitterid = Column(Integer, ForeignKey("users.userid"), primary_key=True)
    pictureid = Column(Integer)
    description = Column(Text)
    user = relationship("User", back_populates="babysitter")
    skills = relationship("BabysitterSkill", back_populates="babysitter")


class Parent(Base):
    __tablename__ = "parent"
    parentid = Column(Integer, ForeignKey("users.userid"), primary_key=True)
    description = Column(Text)
    user = relationship("User", back_populates="parent")
    children = relationship("Children", secondary="parents_childrens", back_populates="parents")


class Children(Base):
    __tablename__ = "children"
    childid = Column(Integer, primary_key=True)
    name = Column(String(255))
    birthdate = Column(Date)
    gender = Column(String(10))
    parents = relationship("Parent", secondary="parents_childrens", back_populates="children")
    needs_association = relationship("ChildrensNeeds", back_populates="child")


class ParentsChildrens(Base):
    __tablename__ = "parents_childrens"

    childid = Column(Integer, ForeignKey("children.childid"), primary_key=True)
    parentid = Column(Integer, ForeignKey("parent.parentid"), primary_key=True)
    # child = relationship("Children", back_populates="parents")
    # parent = relationship("Parent", back_populates="childrens")


class Review(Base):
    __tablename__ = "reviews"

    reviewid = Column(Integer, primary_key=True)
    reviewerid = Column(Integer, ForeignKey("users.userid"))
    reviewedid = Column(Integer, ForeignKey("users.userid"))
    rating = Column(Float)
    flexibilityrating = Column(Float)
    reliabilityrating = Column(Float)
    interpersonalrating = Column(Float)
    comment = Column(Text)
    publicationdate = Column(Date)
    review_text = Column(Text)
    reviewer = relationship("User", foreign_keys=[reviewerid])
    reviewed = relationship("User", foreign_keys=[reviewedid])


class SpecialNeed(Base):
    __tablename__ = "specialneed"

    needid = Column(Integer, primary_key=True)
    needname = Column(String(255))
    children_needs = relationship("ChildrensNeeds", back_populates="need")


class SpecialSkill(Base):
    __tablename__ = "specialskill"

    skillid = Column(Integer, primary_key=True)
    skillname = Column(String(255))


class ChildrensNeeds(Base):
    __tablename__ = "childrens_needs"

    childid = Column(Integer, ForeignKey("children.childid"), primary_key=True)
    needid = Column(Integer, ForeignKey("specialneed.needid"), primary_key=True)
    needrank = Column(Integer)
    child = relationship("Children", back_populates="needs_association")
    need = relationship("SpecialNeed", back_populates="children_needs")


class BabysitterSkill(Base):
    __tablename__ = "babysitterskill"

    skillid = Column(Integer, ForeignKey("specialskill.skillid"), primary_key=True)
    babysitterid = Column(Integer, ForeignKey("babysitter.babysitterid"), primary_key=True)
    skillrank = Column(Integer)
    skill = relationship("SpecialSkill")
    babysitter = relationship("Babysitter", back_populates="skills")


class NeedSkill(Base):
    __tablename__ = "need_skill"

    needid = Column(Integer, ForeignKey("specialneed.needid"), primary_key=True)
    skillid = Column(Integer, ForeignKey("specialskill.skillid"), primary_key=True)
    need = relationship("SpecialNeed")
    skill = relationship("SpecialSkill")


class Favorite(Base):
    __tablename__ = "favorites"

    parentid = Column(Integer, ForeignKey("parent.parentid"), primary_key=True)
    babysitterid = Column(Integer, ForeignKey("babysitter.babysitterid"), primary_key=True)
    parent = relationship("Parent")
    babysitter = relationship("Babysitter")


class Contacted(Base):
    __tablename__ = "contacted"

    contactid = Column(Integer, primary_key=True)
    parentid = Column(Integer, ForeignKey("parent.parentid"))
    babysitterid = Column(Integer, ForeignKey("babysitter.babysitterid"))
    date = Column(Date)


class Scheduler(Base):
    __tablename__ = "scheduler"

    babysitterid = Column(Integer, ForeignKey("babysitter.babysitterid"), primary_key=True)
    dayinweek = Column(String(10), primary_key=True)
    starttime = Column(Time, primary_key=True)
    endtime = Column(Time)
    babysitter = relationship("Babysitter")
