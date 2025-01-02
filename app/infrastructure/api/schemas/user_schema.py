from pydantic import BaseModel, validator
from app.infrastructure.api.schemas.base_schema import ResponseModel


class InputPostChangePassword(BaseModel):
    current_password: str
    new_password: str

    @validator("new_password")
    def passwords_must_be_different(cls, new_password, values):
        current_password = values.get("current_password")
        if current_password and current_password == new_password:
            raise ValueError(
                "The new password must be different from the current password."
            )
        return new_password
