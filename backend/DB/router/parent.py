from typing import List

import crud
import schemas
from database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Parent)
def create_parent(parent: schemas.Parent, db: Session = Depends(get_db)):
    db_parent = crud.get_parent(db, parent_id=parent.parentid)
    if db_parent:
        raise HTTPException(status_code=400, detail="Parent already registered")
    return crud.create_parent(db=db, parent=parent)


@router.get("/{parent_id}", response_model=schemas.Parent)
def read_parent(parent_id: int, db: Session = Depends(get_db)):
    db_parent = crud.get_parent(db, parent_id=parent_id)
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return db_parent


@router.get("/", response_model=List[schemas.Parent])
def read_parents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    parents = crud.get_parents(db, skip=skip, limit=limit)
    return parents
