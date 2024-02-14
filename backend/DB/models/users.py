from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    userid = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    registrationdate = Column(Date)
    city = Column(String(255))
    street = Column(String(255))
    phone = Column(String(15))
