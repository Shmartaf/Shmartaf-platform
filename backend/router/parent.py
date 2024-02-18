from typing import List

from fastapi import APIRouter, HTTPException

from backend.database import models, schemas
from backend.database.dal import DataAccessLayer

router = APIRouter()


dal = DataAccessLayer()


@router.get("/", response_model=List[schemas.ParentRead])
def read_parents(skip: int = 0, limit: int = 10):
    parents = dal.get_all(models.Parent, skip=skip, limit=limit)
    return parents


@router.get("/{parent_id}", response_model=schemas.ParentRead)
def read_parent(parent_id: int):
    parent = dal.get(models.Parent, parent_id)
    if parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return parent


@router.post("/", response_model=schemas.Parent)
def create_parent(parent: schemas.Parent):
    return dal.create(models.Parent, parent)


@router.put("/{parent_id}", response_model=schemas.Parent)
def update_parent(parent_id: int, parent: schemas.Parent):
    db_parent = dal.get(model=models.Parent, id=parent_id)
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return dal.update(models.Parent, parent_id, parent)


@router.delete("/{parent_id}", response_model=schemas.Parent)
def delete_parent(parent_id: int):
    db_parent = dal.get(model=models.Parent, id=parent_id)
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return dal.delete(models.Parent, parent_id)
