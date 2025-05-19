from lib.settings import get_settings
from server import app


@app.get("/")
def root():
    return {"hello": "world"}


@app.get("/settings")
def settings():
    return get_settings()
