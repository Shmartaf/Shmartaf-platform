from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
import crud
import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Babysitter)
def create_babysitter(babysitter: schemas.Babysitter, db: Session = Depends(get_db)):
    db_babysitter = crud.get_babysitter(db, babysitter_id=babysitter.babysitterid)
    if db_babysitter:
        raise HTTPException(status_code=400, detail="Babysitter already registered")
    return crud.create_babysitter(db=db, babysitter=babysitter)

@router.get("/{babysitter_id}", response_model=schemas.BabysitterRead)
def read_babysitter(babysitter_id: int, db: Session = Depends(get_db)):
    db_babysitter = crud.get_babysitter(db, babysitter_id=babysitter_id)
    if db_babysitter is None:
        raise HTTPException(status_code=404, detail="Babysitter not found")
    return db_babysitter

@router.get("/", response_model=List[schemas.BabysitterRead])
def read_babysitters(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    babysitters = crud.get_babysitters(db, skip=skip, limit=limit)
    return babysitters