from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    email: str
    password: str
    first_name: str
    last_name: str
