from typing import List

from fastapi import APIRouter, HTTPException

from backend.database import models, schemas
from backend.database.dal import DataAccessLayer

router = APIRouter()


dal = DataAccessLayer()


@router.get("/", response_model=List[schemas.BabysitterRead])
def read_users(skip: int = 0, limit: int = 10):
    users = dal.get_all(models.User, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.BabysitterRead)
def read_user(user_id: int):
    user = dal.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=schemas.BabysitterRead)
def create_user(user: schemas.User):
    db_user = dal.get(model=models.User, id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return dal.create(models.User, user)


@router.put("/{user_id}", response_model=schemas.BabysitterRead)
def update_user(user_id: int, user: schemas.User):
    db_user = dal.get(model=models.User, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dal.update(models.User, user_id, user)


@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int):
    user = dal.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    dal.delete(models.User, user_id)
    return user
