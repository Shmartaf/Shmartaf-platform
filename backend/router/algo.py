from fastapi import APIRouter, HTTPException
from pydantic import UUID4
#from backend.send_parent_id import get_recommendations_for_parent
from backend.database import models, schemas
from backend.database.dal import DataAccessLayer

router = APIRouter(
    prefix="/algo",
    tags=["algo"],
)


dal = DataAccessLayer()

#@router.get("/{user_id}")
#def getBabysitterFromAlgo(user_id, skip: int = 0, limit: int = 1000) -> list[schemas.BabysitterSchema]:
#    return get_recommendations_for_parent(user_id)