from typing import List

from backend.database import schemas, models
from backend.database.database import Base, get_db
from fastapi import APIRouter, Depends, HTTPException
from backend.database.dal import DataAccessLayer

router = APIRouter()
dal = DataAccessLayer()


@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10):
    return dal.get_all(models.User, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int):
    user = dal.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.User):
    return dal.create(models.User, user)


@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int):
    user = dal.delete(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
