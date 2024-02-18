from backend.database import models
from backend.database import schemas
from sqlalchemy.orm import Session, joinedload
from backend.database.database import get_db, Base


class DataAccessLayer:
    def __init__(self):
        self.db = get_db()

    def get(self, model, id: int):
        return self.db.query(model).filter(model.id == id).first()

    def get_all(self, model, skip: int = 0, limit: int = 100):
        return self.db.query(model).offset(skip).limit(limit).all()

    def create(self, model, schema):
        db_model = model(**schema.dict())
        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)
        return db_model

    def update(self, model, id: int, schema):
        db_model = self.get(model, id)
        for var, value in schema.dict().items():
            setattr(db_model, var, value)
        self.db.commit()
        self.db.refresh(db_model)
        return db_model

    def delete(self, model, id: int):
        db_model = self.get(model, id)
        self.db.delete(db_model)
        self.db.commit()
        return db_model
