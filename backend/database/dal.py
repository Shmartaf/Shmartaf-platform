# from backend.database import models, schemas
from backend.database.database import Database
from backend.logger import ColorLogger, log_decorator


@log_decorator
class DataAccessLayer:
    def __init__(self):
        self.db = Database().SessionLocal()
        self.logger = ColorLogger()

    @log_decorator
    def get(self, model, id: int):
        result = self.db.query(model).filter(model.id == id).first()
        self.logger.log(
            message=f"Get {model.__name__} with id {id}", level="INFO", data=result
        )
        return result

    @log_decorator
    def get_all(self, model, skip: int = 0, limit: int = 100):
        result = self.db.query(model).offset(skip).limit(limit).all()
        self.logger.log(message=f"Get all {model.__name__}", level="INFO", data=result)
        return result

    @log_decorator
    def create(self, model, schema):
        db_model = model(**schema.dict())
        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)
        self.logger.log(
            message=f"Create {model.__name__} with id {db_model.id}",
            level="INFO",
            data=db_model,
        )
        return db_model

    @log_decorator
    def update(self, model, id: int, schema):
        db_model = self.get(model, id)
        for var, value in schema.dict().items():
            setattr(db_model, var, value)
        self.db.commit()
        self.db.refresh(db_model)
        self.logger.log(
            message=f"Update {model.__name__} with id {id}", level="INFO", data=db_model
        )
        return db_model

    def delete(self, model, id: int):
        db_model = self.get(model, id)
        self.db.delete(db_model)
        self.db.commit()
        self.logger.log(
            message=f"Delete {model.__name__} with id {id}", level="INFO", data=db_model
        )
        return db_model

    def aggregate(self, model, id: int, field: str):
        result = self.db.query(model).filter(getattr(model, field) == id).all()
        self.logger.log(
            message=f"Get {model.__name__} with {field} {id}", level="INFO", data=result
        )
        return result
