from contextlib import asynccontextmanager

from fastapi import FastAPI

from lib.settings import get_settings


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # startup
    # 1. attempt to load settings from env
    get_settings()
    yield
    # shutdown


app = FastAPI(lifespan=lifespan)
