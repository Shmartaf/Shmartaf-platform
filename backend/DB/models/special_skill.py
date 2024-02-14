from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SpecialSkill(Base):
    __tablename__ = "specialskill"
    skillid = Column(Integer, primary_key=True)
    skillname = Column(String(255))
