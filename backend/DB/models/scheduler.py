from sqlalchemy import Column, Integer, String, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Scheduler(Base):
    __tablename__ = "scheduler"
    babysitterid = Column(Integer, primary_key=True)
    dayinweek = Column(String(10), primary_key=True)
    starttime = Column(Time, primary_key=True)
    endtime = Column(Time)
