from pydantic import BaseSettings


class Settings(BaseSettings):
    dsn: str


settings = Settings()
