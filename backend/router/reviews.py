from typing import List

from fastapi import APIRouter, HTTPException

from backend.database import models, schemas
from backend.database.dal import DataAccessLayer

router = APIRouter()


dal = DataAccessLayer()


@router.get("/", response_model=List[schemas.ReviewRead])
def read_reviews(skip: int = 0, limit: int = 10):
    reviews = dal.get_all(models.Review, skip=skip, limit=limit)
    return reviews


@router.get("/{review_id}", response_model=schemas.ReviewRead)
def read_review(review_id: int):
    review = dal.get(models.Review, review_id)
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review


@router.post("/", response_model=schemas.ReviewRead)
def create_review(review: schemas.Review):
    return dal.create(models.Review, review)
