from fastapi import FastAPI
from app.main import routes
from fastapi.staticfiles import StaticFiles
app = FastAPI()


# Mount the static directory
app.mount("/static", StaticFiles(directory="app/main/static"), name="static")

app.include_router(routes.router)
