from datetime import datetime
from typing import Any, Optional
from uuid import uuid4

import jwt

from app.shared.auth import constants
from app.shared.auth.auth_class import TokenHandler
from app.shared.auth.exceptions import InvalidTokenError, TokenExpiredError
from app.shared.exceptions import ValidationError
from core.config import settings
from app.shared.utils.core.datetime import get_datetime_now


class JWTToken(TokenHandler):
    @classmethod
    def encode(
        cls,
        payload: dict[str, Any],
        algorithm: Optional[str] = None,
        expires: Optional[datetime] = None,
        type: Optional[str] = None,
        **kwargs,
    ):
        alg = algorithm or "HS256"
        typ = type or "access"
        kid = kwargs.get("kid", uuid4().hex)

        if typ.upper() not in settings.TOKEN_TYPES_LIST:
            raise ValueError(f"type {typ} not configured")

        if not expires:
            conf = next(filter(lambda conf: conf["type"] == typ, settings.TOKEN_TYPES))
            expires = get_datetime_now() + conf["expiration"]

        payload.update(exp=expires)
        headers = {"alg": alg, "typ": typ, "kid": kid}
        token = jwt.encode(payload, settings.SECRET_KEY, headers=headers)
        return token

    @classmethod
    def decode(cls, token: str, **kwargs) -> dict[str, Any]:
        try:
            token = token.split(" ").pop()
            headers = jwt.get_unverified_header(jwt=token)
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[headers.get("alg")],
            )
            payload |= headers
            if not constants.TokenTypes.has_value(payload.get("typ")):
                raise ValidationError("Invalid Token Type")
            return payload
        except jwt.ExpiredSignatureError as e:
            raise TokenExpiredError(str(e))
        except jwt.InvalidSignatureError as e:
            raise InvalidTokenError(str(e))
        except Exception as e:
            raise InvalidTokenError(f"Problem with token: {str(e)}")
