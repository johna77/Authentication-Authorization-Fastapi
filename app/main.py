from fastapi import FastAPI
from app import models
from .router import login, regis
from app.database import engine
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(login.router)
app.include_router(regis.router)