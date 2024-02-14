from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Babysitter(Base):
    __tablename__ = "babysitter"
    babysitterid = Column(Integer, primary_key=True)
    pictureid = Column(Integer)
    description = Column(String)
