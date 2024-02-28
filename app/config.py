from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    admin_create_key: str
    origins: List[str]


settings = Settings()
