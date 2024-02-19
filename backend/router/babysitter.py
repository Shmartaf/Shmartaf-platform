from typing import List

from fastapi import APIRouter, HTTPException

from backend.database import models, schemas
from backend.database.dal import DataAccessLayer

router = APIRouter()


dal = DataAccessLayer()


@router.get("/", response_model=List[schemas.BabysitterRead])
def read_users(skip: int = 0, limit: int = 10):
    users = dal.get_all(models.Babysitter, skip=skip, limit=limit)
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


@router.get("/reviews/{user_id}", response_model=List[schemas.ReviewRead])
def read_reviews_by_babysitter(user_id: int):
    reviews = dal.aggregate(models.Review, id=user_id, field="reviewedid")
    return reviews


@router.post("/reviews/{user_id}", response_model=schemas.ReviewRead)
def create_review_on_babysitter(user_id: int, review: schemas.Review):
    return dal.create(models.Review, review)


@router.get("/schedulers/{user_id}", response_model=List[schemas.Scheduler])
def read_schedulers_by_babysitter(user_id: int):
    schedulers = dal.aggregate(models.Scheduler, id=user_id, field="babysitterid")
    return schedulers
