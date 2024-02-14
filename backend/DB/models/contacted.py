from sqlalchemy import Column, Date, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contacted(Base):
    __tablename__ = "contacted"
    contactid = Column(Integer, primary_key=True)
    parentid = Column(Integer)
    babysitterid = Column(Integer)
    date = Column(Date)
