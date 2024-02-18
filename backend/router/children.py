from typing import List

import crud
import schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, DataError, OperationalError
router = APIRouter()
children_crud = crud.Children()

@router.post("/", response_model=schemas.Children)
def create_children(children: schemas.Children):
    try:
        db_children = children_crud.get_children(child_id=children.childid)
        if db_children:
            raise HTTPException(status_code=400, detail="Children already registered")
        return children_crud.create_children(children=children)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    except (SQLAlchemyError, IntegrityError, DataError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")

@router.get("/{child_id}", response_model=schemas.Children)
def read_children(child_id: int):
    try:
        db_children = children_crud.get_children(child_id=child_id)
        if db_children is None:
            raise HTTPException(status_code=404, detail="Children not found")
        return db_children
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")

@router.get("/", response_model=List[schemas.ChildrenRead])
def read_childrens(skip: int = 0, limit: int = 10):
    try:
        childrens = children_crud.get_childrens(skip=skip, limit=limit)
        return childrens
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
