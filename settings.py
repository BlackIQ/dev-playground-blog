# Pydantic Settings
from pydantic_settings import BaseSettings, SettingsConfigDict


# Settings Class
class Settings(BaseSettings):
    # PostgreSQL URL
    postgres_url: str = ""

    model_config = SettingsConfigDict(env_file=".env")


# Run settings
settings = Settings()
