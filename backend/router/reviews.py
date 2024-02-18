from typing import List
import crud
import schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, DataError, OperationalError

router = APIRouter()

reviews_crud = crud.Review()
@router.post("/", response_model=schemas.Review)
def create_review(review: schemas.Review):
    db_review = reviews_crud.get_review(review_id=review.reviewid)
    if db_review:
        raise HTTPException(status_code=400, detail="Review already registered")
    try:
        return reviews_crud.create_review(review=review)
    except (SQLAlchemyError, IntegrityError, DataError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{review_id}", response_model=schemas.ReviewRead)
def read_review(review_id: int):
    try:
        db_review = reviews_crud.get_review(review_id=review_id)
        if db_review is None:
            raise HTTPException(status_code=404, detail="Review not found")
        return db_review
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/", response_model=List[schemas.ReviewRead])
def read_reviews(skip: int = 0, limit: int = 10):
    try:
        reviews = reviews_crud.get_reviews(skip=skip, limit=limit) 
        return reviews
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/babysitter/{babysitter_id}", response_model=List[schemas.ReviewRead])
def read_reviews_by_babysitter(babysitter_id: int):
    try:
        reviews = reviews_crud.get_reviews_by_babysitter(babysitter_id=babysitter_id)
        return reviews
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/parent/{parent_id}", response_model=List[schemas.ReviewRead])
def read_reviews_by_parent(parent_id: int):
    try:
        reviews = reviews_crud.get_reviews_by_parent(parent_id=parent_id)
        return reviews
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
