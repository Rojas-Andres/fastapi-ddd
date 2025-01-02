from typing import Annotated
from fastapi import Depends, HTTPException, status, Request
import json
import os
from app.shared.auth.jwt_handler import JWTToken
from app.infrastructure.api.schemas.base_schema import CurrentUser
import jwt


class RoleChecker:
    def __init__(
        self,
        allowed_roles,
    ):
        """
        Initialize the RoleChecker class.
        """
        self.allowed_roles = set(allowed_roles)
        self.jwt_token = JWTToken()

    def __call__(self, request: Request):
        """
        Check if the user has the necessary roles to access the endpoint.
        """
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token is missing",
            )
        try:
            user_data = self.jwt_token.decode(token)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
        return CurrentUser(user_id=user_data["user_id"])
