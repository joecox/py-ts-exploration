import os
from functools import cache
from typing import Literal

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(frozen=True)

    environment: Literal["local", "test", "prod"]
    pg_dsn: PostgresDsn


@cache
def get_settings():
    env = os.environ.get("ENV")
    return Settings(_env_file=f".env.{env}", environment=env)
