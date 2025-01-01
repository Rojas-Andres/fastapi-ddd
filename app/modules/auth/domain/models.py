from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID


DEFAULT_PREFIX_TOKEN_TYPE = "Bearer"


@dataclass
class User:
    id: Optional[int] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    status: Optional[str] = None
    is_staff: Optional[bool] = False
    last_login: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    locked_until: Optional[datetime] = None
    failed_attempts: Optional[int] = 0
