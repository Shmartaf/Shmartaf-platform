from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Children(Base):
    __tablename__ = "children"
    childid = Column(Integer, primary_key=True)
    name = Column(String(255))
    birthdate = Column(Date)
    gender = Column(String(10))
