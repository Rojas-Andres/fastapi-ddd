from typing import Generic, List, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    """
    Modelo genérico para las respuestas de la API.
    """

    data: T
