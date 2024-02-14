from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NeedSkill(Base):
    __tablename__ = "need_Skill"
    needid = Column(Integer, primary_key=True)
    skillid = Column(Integer, primary_key=True)
