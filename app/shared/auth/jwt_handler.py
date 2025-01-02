from datetime import datetime
from typing import Any, Optional
from uuid import uuid4

import jwt

from app.shared.auth import constants
from app.shared.auth.auth_class import TokenHandler
from app.shared.auth.exceptions import InvalidTokenError, TokenExpiredError
from app.shared.exceptions import ValidationError
from app.core.config import settings
from app.shared.utils.core.datetime import get_datetime_now


class JWTToken(TokenHandler):
    @classmethod
    def encode(
        cls,
        payload: dict[str, Any],
        algorithm: Optional[str] = None,
        expires: Optional[datetime] = None,
        **kwargs,
    ):
        alg = algorithm or "HS256"
        kid = kwargs.get("kid", uuid4().hex)
        payload.update(exp=expires)
        headers = {"alg": alg, "typ": "access", "kid": kid}
        token = jwt.encode(payload, settings.SECRET_KEY, headers=headers)
        return token

    @classmethod
    def decode(cls, token: str, **kwargs) -> dict[str, Any]:
        try:
            headers = jwt.get_unverified_header(jwt=token)
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[headers.get("alg")],
            )
            payload |= headers
            return payload
        except jwt.ExpiredSignatureError as e:
            raise TokenExpiredError(str(e))
        except jwt.InvalidSignatureError as e:
            raise InvalidTokenError(str(e))
        except Exception as e:
            raise InvalidTokenError(f"Problem with token: {str(e)}")
