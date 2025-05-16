from fastapi import FastAPI

from lib.other import other
from lib.settings import settings

app = FastAPI()


@app.get("/")
def root():
    return {"hello": other()}


@app.get("/settings")
def get_settings():
    return settings
