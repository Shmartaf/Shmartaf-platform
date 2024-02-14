from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ChildrensNeeds(Base):
    __tablename__ = "childrens_needs"
    childid = Column(Integer, primary_key=True)
    needid = Column(Integer, primary_key=True)
    needrank = Column(Integer)
