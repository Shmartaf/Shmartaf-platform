from typing import List

from fastapi import APIRouter, HTTPException

from backend.database import models, schemas
from backend.database.dal import DataAccessLayer

router = APIRouter()

dal = DataAccessLayer()


@router.get("/", response_model=List[schemas.Scheduler])
def read_schedulers(skip: int = 0, limit: int = 10):
    schedulers = dal.get_all(models.Scheduler, skip=skip, limit=limit)
    return schedulers


@router.get("/{scheduler_id}", response_model=schemas.Scheduler)
def read_scheduler(scheduler_id: int):
    scheduler = dal.get(models.Scheduler, scheduler_id)
    if scheduler is None:
        raise HTTPException(status_code=404, detail="Scheduler not found")
    return scheduler


@router.post("/", response_model=schemas.Scheduler)
def create_scheduler(scheduler: schemas.Scheduler):
    return dal.create(models.Scheduler, scheduler)


@router.put("/{scheduler_id}", response_model=schemas.Scheduler)
def update_scheduler(scheduler_id: int, scheduler: schemas.Scheduler):
    db_scheduler = dal.get(model=models.Scheduler, id=scheduler_id)
    if db_scheduler is None:
        raise HTTPException(status_code=404, detail="Scheduler not found")
    return dal.update(models.Scheduler, scheduler_id, scheduler)


@router.delete("/{scheduler_id}", response_model=schemas.Scheduler)
def delete_scheduler(scheduler_id: int):
    db_scheduler = dal.get(model=models.Scheduler, id=scheduler_id)
    if db_scheduler is None:
        raise HTTPException(status_code=404, detail="Scheduler not found")
    return dal.delete(models.Scheduler, scheduler_id)


@router.get("/babysitter/{babysitter_id}", response_model=List[schemas.Scheduler])
def read_schedulers_by_babysitter(babysitter_id: int):
    schedulers = dal.get_schedulers_by_babysitter(babysitter_id=babysitter_id)
    return schedulers
