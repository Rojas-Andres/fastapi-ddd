"""
Config file
"""

import os
from typing import Any

from dotenv import load_dotenv
from datetime import timedelta

load_dotenv(".env")


class Settings:
    """
    A class that encapsulates environment configuration variables.

    The Settings class retrieves sensitive configuration values such as API keys,
    database connection details, and other environment-specific settings from
    environment variables. Default values are provided if the environment variables
    are not set."""

    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret_key")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "test")
    DATABASE_USER: str = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "postgres")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT", "5432")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "postgres")

    if ENVIRONMENT == "test":
        DATABASE_URL = "sqlite:///test.db"
    else:
        DATABASE_URL: str = os.getenv(
            "DATABASE_URL",
            f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}",
        )

    TOKEN_ALGORITHM = "HS256"
    TOKEN_MINUTES_EXPIRATION = 120
    COMMAND_TOKEN_MINUTES_EXPIRATION = 120
    COMMAND_TYPE_TOKEN = "Bearer"
    TOKEN_INFINITE_MINUTES_EXPIRATION = 99999999

    TOKEN_TYPES: list[dict[str, Any]] = [
        {
            "type": "access",
            "expiration": timedelta(minutes=TOKEN_MINUTES_EXPIRATION),
        }
    ]
    TOKEN_TYPES_LIST = [
        token_type.get("type").upper()
        for token_type in TOKEN_TYPES  # type: ignore
    ]


settings = Settings()
