from pydantic import BaseModel
from app.infrastructure.api.schemas.base_schema import ResponseModel


class UserSchema(BaseModel):
    id: int
    email: str
    password: str
    first_name: str
    last_name: str


class UserCreateReturn(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str


class InputPostUserLogin(BaseModel):
    email: str
    password: str


class OutputPostUserLogin(BaseModel):
    jwt: str


class CreateUserReturn(ResponseModel[UserCreateReturn]):
    pass


class OutputPostUserLoginReturn(ResponseModel[OutputPostUserLogin]):
    pass
