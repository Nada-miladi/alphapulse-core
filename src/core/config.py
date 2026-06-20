import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AlphaPulse Core"
    ENVIRONMENT: str = "development"

    # Enforce that these API keys must be strings present in the environment
    GROQ_API_KEY: str
    ALPHA_VANTAGE_API_KEY: str

    # Configuration telling Pydantic to scan the root directory for a .env file
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


# Instantiate a global configuration object to import across our backend modules
settings = Settings()
