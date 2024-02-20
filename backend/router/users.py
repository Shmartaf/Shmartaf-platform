from fastapi import APIRouter, HTTPException
from pydantic import UUID4

from backend.database import models, schemas
from backend.database.dal import DataAccessLayer
from backend.logger import ColorLogger

router = APIRouter(
    prefix="/users",
    tags=["users"],
)
logger = ColorLogger()

dal = DataAccessLayer()


@router.get("/")
def get_users(skip: int = 0, limit: int = 10) -> list[schemas.UserSchema]:
    return dal.get_all(models.User, skip=skip, limit=limit)


@router.get("/{user_id}")
def get_user(user_id: UUID4) -> schemas.UserSchema:
    if user := dal.get(model=models.User, id=user_id):
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post("/")
def create_user(user: schemas.UserSchema) -> schemas.UserSchema:
    return dal.create(models.User, user)


@router.put("/{user_id}")
def update_user(
    user_id: UUID4,
    user: schemas.UserSchema,
) -> schemas.UserSchema:
    return dal.update(models.User, user_id, user)


@router.delete("/{user_id}")
def delete_user(user_id: UUID4) -> schemas.UserSchema:
    return dal.delete(models.User, user_id)
