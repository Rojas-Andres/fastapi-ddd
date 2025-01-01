from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
    if "sqlite" in settings.DATABASE_URL
    else {},
)
Base = declarative_base()

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        settings.DATABASE_URL,
        isolation_level="REPEATABLE READ"
        if "sqlite" not in settings.DATABASE_URL
        else None,
        echo=True,
    )
)
