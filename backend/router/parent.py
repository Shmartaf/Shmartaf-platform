from typing import List

from backend.database import schemas,models
from backend.database.database import Database
from fastapi import APIRouter, Depends, HTTPException
from backend.database.dal import DataAccessLayer

router = APIRouter()


dal = DataAccessLayer()

@router.get("/", response_model=List[schemas.ParentRead])
def read_parents(skip: int = 0, limit: int = 10):
    try:
        parents = dal.get_all(models.Parent, skip=skip, limit=limit)
        return parents
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request") from e

@router.get("/{parent_id}", response_model=schemas.ParentRead)
def read_parent(parent_id: int):
    try:
        parent = dal.get(models.Parent, parent_id)
        if parent is None:
            raise HTTPException(status_code=404, detail="Parent not found")
        return parent
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request") from e

@router.post("/", response_model=schemas.Parent)
def create_parent(parent: schemas.Parent):
    try:
        return dal.create(models.Parent, parent)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except (SQLAlchemyError, DataError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request") from e
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Parent already registered") from e
    

@router.put("/{parent_id}", response_model=schemas.Parent)
def update_parent(parent_id: int, parent: schemas.Parent):
    try:
        db_parent = dal.get(model=models.Parent, id=parent_id)
        if db_parent is None:
            raise HTTPException(status_code=404, detail="Parent not found")
        return dal.update(models.Parent, parent_id, parent)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request") from e

@router.delete("/{parent_id}", response_model=schemas.Parent)
def delete_parent(parent_id: int):
    try:
        db_parent = dal.get(model=models.Parent, id=parent_id)
        if db_parent is None:
            raise HTTPException(status_code=404, detail="Parent not found")
        return dal.delete(models.Parent, parent_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request") from e

