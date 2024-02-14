from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SpecialNeed(Base):
    __tablename__ = "specialNeed"
    needid = Column(Integer, primary_key=True)
    needname = Column(String(255))
