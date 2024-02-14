from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BabysitterSkill(Base):
    __tablename__ = "babysitterskill"
    skillid = Column(Integer, primary_key=True)
    babysitterid = Column(Integer, primary_key=True)
    skillrank = Column(Integer)
