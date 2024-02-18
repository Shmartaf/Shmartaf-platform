import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from backend.database.models import Base
from backend.database.database import engine
from router import users, roles
from dotenv import load_dotenv

app = FastAPI(
    title="FastAPI",
    description="FastAPI with PostgreSQL",
    version="0.1.0",
    debug=True,
)


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    app.include_router(
        users.router,
        prefix="/users",
        tags=["users"],
    )

    app.include_router(
        roles.router,
        prefix="/roles",
        tags=["roles"],
    )

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )
