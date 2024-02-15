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

@router.post("/", response_model=schemas.Children)
def create_children(children: schemas.Children, db: Session = Depends(get_db)):
    db_children = crud.get_children(db, children_id=children.childrenid)
    if db_children:
        raise HTTPException(status_code=400, detail="Children already registered")
    return crud.create_children(db=db, children=children)

@router.get("/{children_id}", response_model=schemas.ChildrenRead)
def read_children(children_id: int, db: Session = Depends(get_db)):
    db_children = crud.get_children(db, child_id=children_id)
    if db_children is None:
        raise HTTPException(status_code=404, detail="Children not found")
    return db_children

@router.get("/", response_model=List[schemas.ChildrenRead])
def read_childrens(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    childrens = crud.get_childrens(db, skip=skip, limit=limit)
    return childrens


