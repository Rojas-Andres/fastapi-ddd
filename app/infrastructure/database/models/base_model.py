"""
Base model
"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.infrastructure.database.db import Base


class BaseModel(Base):
    """
    Abstract base model that provides common fields for all models.

    This class defines common attributes such as `id`, `created_at`, `updated_at`,
    `created_by`, `updated_by`, `deleted_at`, and `deleted_by` that can be inherited
    by other models in the database. It automatically handles the generation of UUIDs
    and timestamps for creation, updates, and deletions."""

    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    deleted_at = Column(DateTime, nullable=True)
