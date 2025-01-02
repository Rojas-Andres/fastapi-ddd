from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Optional, TypeVar
from passlib.context import CryptContext


Token = TypeVar("Token", bound=str)


class TokenHandler(ABC):
    @abstractmethod
    def encode(
        self,
        payload: dict[str, Any],
        algorithm: Optional[str] = None,
        expires: Optional[datetime] = None,
        **kwargs,
    ) -> Token:  # type: ignore
        """Register a token with parameters"""
        raise NotImplementedError("Encode method of TokenHandler not implemented")

    @abstractmethod
    def decode(self, token: str, **kwargs) -> dict[str, Any]:
        """Extract info from a signed object or token"""
        raise NotImplementedError("Decode method of TokenHandler not implemented")


class HasherAbstract(ABC):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @abstractmethod
    def verify_password(
        self,
        plain_password: str,
        hashed_password: str,
        **kwargs,
    ) -> str:  # type: ignore
        """Register a token with parameters"""
        raise NotImplementedError(
            "verify_password method of HasherAbstract not implemented"
        )

    @abstractmethod
    def get_password_hash(self, password: str, **kwargs) -> str:
        """Extract info from a signed object or token"""
        raise NotImplementedError(
            "get_password_hash method of HasherAbstract not implemented"
        )

    @abstractmethod
    def generate_random_hash(self, **kwargs) -> str:
        """Generate a random hash"""
        raise NotImplementedError(
            "Generate random hash method of HasherAbstract not implemented"
        )

    @abstractmethod
    def get_password_hash_sha1(self, **kwargs) -> str:
        """Generate a random hash"""
        raise NotImplementedError(
            "get_password_hash_sha1 method of HasherAbstract not implemented"
        )
