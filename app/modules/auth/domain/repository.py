import abc
from typing import Generic, Optional, TypeVar

from app.modules.auth.domain import models

_M = TypeVar("_M")


class AbstractAuthRepository(abc.ABC, Generic[_M]):
    @abc.abstractmethod
    def get_by_id(self, user_id: str) -> Optional[models.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_email(self, email: str) -> Optional[models.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, user: models.User) -> models.User:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, user: models.User) -> models.User | None:
        raise NotImplementedError

    @abc.abstractmethod
    def change_password(self, user: _M, password: str) -> None:
        raise NotImplementedError
