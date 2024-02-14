from sqlalchemy import Column, Date, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Reviews(Base):
    __tablename__ = "reviews"
    reviewid = Column(Integer, primary_key=True)
    reviewerid = Column(Integer)
    reviewedid = Column(Integer)
    rating = Column(Float)
    flexibilityrating = Column(Float)
    reliabilityrating = Column(Float)
    interpersonalrating = Column(Float)
    comment = Column(String)
    publicationdate = Column(Date)
