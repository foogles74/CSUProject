from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Optional


class Settings(BaseSettings):
    BOT_TOKEN: Optional[str] = None
    SERVER_IP: Optional[str] = None
    SERVER_USER: Optional[str] = None
    SERVER_PASS: Optional[str] = None
    model_config = SettingsConfigDict(env_file='../../.env')


@lru_cache()
def get_settings() -> Settings:
    return Settings()