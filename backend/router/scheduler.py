from typing import List
import crud
import schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, DataError, OperationalError

router = APIRouter()

scheduler_crud = crud.Scheduler()
@router.post("/", response_model=schemas.Scheduler)
def create_scheduler(scheduler: schemas.Scheduler):
    try:
        db_scheduler = scheduler_crud.get_scheduler(scheduler_id=scheduler.schedulerid)
        if db_scheduler:
            raise HTTPException(status_code=400, detail="Scheduler already registered")
        return scheduler_crud.create_scheduler(scheduler=scheduler)
    except (SQLAlchemyError, IntegrityError, DataError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{scheduler_id}", response_model=schemas.Scheduler)
def read_scheduler(scheduler_id: int):
    try:
        db_scheduler = scheduler.get_scheduler(scheduler_id=scheduler_id)
        if db_scheduler is None:
            raise HTTPException(status_code=404, detail="Scheduler not found")
        return db_scheduler
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/", response_model=List[schemas.SchedulerRead])
def read_schedulers(skip: int = 0, limit: int = 10):
    try:
        schedulers = scheduler_crud.get_schedulers(skip=skip, limit=limit) 
        return schedulers
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/babysitter/{babysitter_id}", response_model=List[schemas.SchedulerRead])
def read_schedulers_by_babysitter(babysitter_id: int):
    try:
        schedulers = scheduler_crud.get_schedulers_by_babysitter(babysitter_id=babysitter_id)
        return schedulers
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@router.get("/time/{time}", response_model=List[schemas.SchedulerRead])
def read_schedulers_by_time(time: str):
    try:
        schedulers = scheduler_crud.get_schedulers_by_time(time=time)
        return schedulers
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/day/{day}", response_model=List[schemas.SchedulerRead])
def read_schedulers_by_day(day: str):
    try:
        schedulers = scheduler_crud.get_schedulers_by_day(day=day)
        return schedulers
    except (SQLAlchemyError, OperationalError):
        raise HTTPException(status_code=400, detail="Invalid request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


