from typing import List

import crud
import schemas
from fastapi import APIRouter, HTTPException

router = APIRouter()
children_crud = crud.Children()


@router.post("/", response_model=schemas.Children)
def create_children(children: schemas.Children):
    db_children = children_crud.get_children(child_id=children.childid)
    if db_children:
        raise HTTPException(status_code=400, detail="Children already registered")
    return children_crud.create_children(children=children)


@router.get("/{child_id}", response_model=schemas.Children)
def read_children(child_id: int):
    db_children = children_crud.get_children(child_id=child_id)
    if db_children is None:
        raise HTTPException(status_code=404, detail="Children not found")
    return db_children


@router.get("/", response_model=List[schemas.ChildrenRead])
def read_childrens(skip: int = 0, limit: int = 10):
    childrens = children_crud.get_childrens(skip=skip, limit=limit)
    return childrens
