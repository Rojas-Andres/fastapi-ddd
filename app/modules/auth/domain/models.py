from pydantic import BaseModel, EmailStr


DEFAULT_PREFIX_TOKEN_TYPE = "Bearer"


class User(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str
