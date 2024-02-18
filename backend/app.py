import uvicorn
from database.database import Database
from fastapi import FastAPI

# from router import babysitter, children, parent, users, reviews, scheduler
from router import babysitter, parent, users

Database().create_all()

app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(parent.router, prefix="/parents", tags=["parents"])
app.include_router(babysitter.router, prefix="/babysitters", tags=["babysitters"])
# app.include_router(children.router, prefix="/children", tags=["children"])
# app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
# app.include_router(scheduler.router, prefix="/schedules", tags=["schedules"])

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )
