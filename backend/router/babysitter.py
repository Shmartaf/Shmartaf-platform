from typing import List

from backend.database import schemas,models
from backend.database.database import Database
from fastapi import APIRouter, Depends, HTTPException
from backend.database.dal import DataAccessLayer

router = APIRouter()


dal = DataAccessLayer()

@router.get("/", response_model=List[schemas.BabysitterRead])
def read_users(skip: int = 0, limit: int = 10):
    try:
        users = dal.get_all(models.User, skip=skip, limit=limit)
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request") from e
    
@router.get("/{user_id}", response_model=schemas.BabysitterRead)
def read_user(user_id: int):
    try:
        user = dal.get(models.User, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request") from e

@router.post("/", response_model=schemas.Babysitter)
def create_user(user: schemas.User):
    try:
        db_user = dal.get(model=models.User, id=user.id)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return dal.create(models.User, user)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except (SQLAlchemyError, IntegrityError, DataError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request") from e

@router.put("/{user_id}", response_model=schemas.Babysitter)
def update_user(user_id: int, user: schemas.User):
    try:
        db_user = dal.get(model=models.User, id=user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return dal.update(models.User, user_id, user)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request") from e

@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int):
    try:
        user = dal.get(models.User, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        dal.delete(models.User, user_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request") from e
