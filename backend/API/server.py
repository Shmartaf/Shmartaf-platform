import fastapi


app = fastapi.FastAPI()
router = fastapi.APIRouter()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/parents")
def read_parents():
    return {"parents": "parents"}