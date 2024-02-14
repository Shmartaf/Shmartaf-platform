from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Parent(Base):
    __tablename__ = "parent"
    parentid = Column(Integer, primary_key=True)
    description = Column(String)
