from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Tirelire Web Backend"
    description: str = ""
    version: str = "1.0.0"


settings = Settings()
