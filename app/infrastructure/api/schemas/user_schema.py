from pydantic import BaseModel
from app.infrastructure.api.schemas.base_schema import ResponseModel


class InputPostChangePassword(BaseModel):
    current_password: str
    new_password: str
