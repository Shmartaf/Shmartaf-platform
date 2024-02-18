from typing import List


import schemas
from fastapi import APIRouter, HTTPException
from backend.database.dal import DataAccessLayer

router = APIRouter()

dal = DataAccessLayer()


@router.get("/", response_model=List[schemas.ChildrenRead])
def read_parents(skip: int = 0, limit: int = 10):
    parents = dal.get_all(models.Children, skip=skip, limit=limit)
    return parents


@router.get("/{parent_id}", response_model=schemas.ChildrenRead)
def read_parent(parent_id: int):
    parent = dal.get(models.Children, parent_id)
    if parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return parent
