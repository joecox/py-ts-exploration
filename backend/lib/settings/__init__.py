import os
from typing import Literal

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: Literal["local", "test", "prod"]
    pg_dsn: PostgresDsn


env = os.environ.get("ENV")
settings = Settings(_env_file=f".env.{env}", environment=env)
