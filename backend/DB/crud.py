import models
import schemas
from sqlalchemy.orm import Session


def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.userid == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    db_user = models.Users(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_babysitter(db: Session, babysitter_id: int):
    return db.query(models.Babysitter).filter(models.Babysitter.babysitterid == babysitter_id).first()


def get_babysitters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Babysitter).offset(skip).limit(limit).all()


def create_babysitter(db: Session, babysitter: schemas.Babysitter):
    db_babysitter = models.Babysitter(**babysitter.dict())
    db.add(db_babysitter)
    db.commit()
    db.refresh(db_babysitter)
    return db_babysitter


def get_parent(db: Session, parent_id: int):
    return db.query(models.Parent).filter(models.Parent.parentid == parent_id).first()


def get_parents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Parent).offset(skip).limit(limit).all()


def create_parent(db: Session, parent: schemas.Parent):
    db_parent = models.Parent(**parent.dict())
    db.add(db_parent)
    db.commit()
    db.refresh(db_parent)
    return db_parent
