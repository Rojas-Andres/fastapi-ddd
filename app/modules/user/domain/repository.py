import abc
from typing import Generic, Optional, TypeVar

from app.modules.auth.domain import models

_M = TypeVar("_M")


class AbstractUserRepository(abc.ABC, Generic[_M]):
    @abc.abstractmethod
    def get_by_id(self, user_id: str) -> Optional[models.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def change_password(
        self, user_id: int, current_password: str, new_password: str
    ) -> Optional[models.User]:
        raise NotImplementedError
