from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Text, Time
from sqlalchemy.orm import relationship
from backend.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    gender = Column(String(10))
    email = Column(String(255))
    password = Column(String(255))
    registrationdate = Column(Date)
    city = Column(String(255))
    street = Column(String(255))
    phone = Column(String(15))
    roleid = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    rolename = Column(String(255))
    users = relationship("User", back_populates="role")
