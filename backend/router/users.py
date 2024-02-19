from typing import List

from fastapi import APIRouter, HTTPException

from backend.database import models, schemas
from backend.database.dal import DataAccessLayer
from backend.logger import ColorLogger

router = APIRouter()
logger = ColorLogger()

dal = DataAccessLayer()


@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10):
    users = dal.get_all(models.User, skip=skip, limit=limit)
    logger.log("Users has retrieved succesfuly", "INFO", data=users)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int):
    user = dal.get(models.User, user_id)
    if user is None:
        logger.log(f"User not found {user_id}", "ERROR", data=user)
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.User):
    db_user = dal.get(model=models.User, id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return dal.create(models.User, user)


@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.User):
    db_user = dal.get(model=models.User, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dal.update(models.User, user_id, user)


@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int):
    db_user = dal.get(model=models.User, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dal.delete(models.User, user_id)
