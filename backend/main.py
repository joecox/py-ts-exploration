from fastapi import FastAPI

from lib.other import other

app = FastAPI()


@app.get("/")
def root():
    return {"hello": other()}
