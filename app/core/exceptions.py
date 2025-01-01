"""
Base custom exceptions
"""

from fastapi import status


class ValidationError(Exception):
    """
    Custom exception for validation errors
    """

    def __init__(self, detail: str) -> None:
        """
        Initialize the ValidationError

        Args:
            detail (str): The detail of the error
        """

        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = detail


class IntegrityError(Exception):
    """
    Custom exception for integrity errors
    """

    def __init__(self, detail: str) -> None:
        """
        Initialize the IntegrityError

        Args:
            detail (str): The detail of the error
        """

        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = detail


class CustomAPIException(Exception):
    """
    Custom exception for general API errors
    """

    def __init__(self, detail: str, status_code: int) -> None:
        """
        Initialize the CustomAPIException

        Args:
            detail (str): The detail of the error
            status_code (int): The status code of the error
        """

        self.status_code = status_code
        self.detail = detail


class ObjectNotFoundException(Exception):
    """
    ObjectNotFoundException exception for general API errors
    """
