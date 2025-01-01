"""
Error handling middleware
"""

import logging
from typing import Callable

from fastapi import Request, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, Response

from app.core.exceptions import (
    CustomAPIException,
    IntegrityError,
    ObjectNotFoundException,
    ValidationError,
)


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    """
    Middleware for centralized error handling
    """

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request and handle any exceptions

        Args:
            request (Request): The request to process
            call_next: The next middleware to call

        Returns:
            Response: The response from the next middleware
        """
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        }
        try:
            response: Response = await call_next(request)
            for key, value in headers.items():
                response.headers[key] = value
            return response

        except ValidationError as exc:
            logging.error("ValidationError: %s", exc)
            return JSONResponse(
                {
                    "success": False,
                    "message": str(exc.detail),
                    "code": "VALIDATION_ERROR",
                    "field": getattr(exc, "field", None),
                    "value": getattr(exc, "value", None),
                },
                status_code=exc.status_code,
                headers=headers,
            )

        except ValueError as exc:
            logging.error("ValueError: %s", exc)
            return JSONResponse(
                {"success": False, "message": str(exc), "code": "VALIDATION_ERROR"},
                status_code=status.HTTP_400_BAD_REQUEST,
                headers=headers,
            )

        except IntegrityError as exc:
            logging.error("IntegrityError: %s", exc)
            return JSONResponse(
                {"success": False, "message": "Integrity error", "code": "INT001"},
                status_code=exc.status_code,
                headers=headers,
            )

        except CustomAPIException as exc:
            logging.error("CustomAPIException: %s", exc)
            return JSONResponse(
                {
                    "success": False,
                    "message": str(exc.detail),
                    "code": str(exc.status_code),
                },
                status_code=exc.status_code,
                headers=headers,
            )
        except ObjectNotFoundException as exc:
            logging.error("ObjectNotFound: %s", exc)
            return JSONResponse(
                {"success": True, "message": str(exc), "code": "NOT_FOUND"},
                status_code=status.HTTP_400_BAD_REQUEST,
                headers=headers,
            )
        except Exception as exc:
            logging.error("Unexpected error: %s", exc)
            return JSONResponse(
                {
                    "success": False,
                    "message": "An unexpected error occurred",
                    "details": str(exc),
                },
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                headers=headers,
            )
