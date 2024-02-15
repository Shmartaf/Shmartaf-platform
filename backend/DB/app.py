import uvicorn
from database import Base, SessionLocal, engine
from fastapi import FastAPI
from router import babysitter, children, parent, users


# models.Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(parent.router, prefix="/parents", tags=["parents"])
app.include_router(babysitter.router, prefix="/babysitters", tags=["babysitters"])
app.include_router(children.router, prefix="/children", tags=["children"])
# Dependency


@app.on_event("startup")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.User, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )
