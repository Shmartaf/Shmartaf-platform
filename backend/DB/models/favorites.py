from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Favorite(Base):
    __tablename__ = "favorites"
    parentid = Column(Integer, primary_key=True)
    babysitterid = Column(Integer, primary_key=True)
