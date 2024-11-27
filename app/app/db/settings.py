import pika
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Optional


class Settings(BaseSettings):
    DB_HOST: Optional[str] = None
    DB_PORT: Optional[int] = None
    DB_USER: Optional[str] = None
    DB_PASS: Optional[str] = None
    DB_NAME: Optional[str] = None
    SECRET_KEY: Optional[str] = None

    @property
    def DATABASE_URL_psycopg(self):
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='../../.env')

    @property
    def rabbit_connect_params(self):
        return pika.ConnectionParameters(
            host=self.DB_HOST,
            port=5672,
            virtual_host='/',
            credentials=pika.PlainCredentials(
                username=self.DB_USER,
                password=self.DB_PASS
            )
        )


@lru_cache()
def get_settings() -> Settings:
    return Settings()