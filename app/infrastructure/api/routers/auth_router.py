from fastapi import APIRouter
from app.modules.auth import bootstrap
from app.modules.auth.domain import commands
from app.modules.auth.domain.models import User
from app.infrastructure.api.schemas.auth_schema import (
    CreateUserReturn,
    OutputPostUserLoginReturn,
    InputPostUserLogin,
)

router = APIRouter()


@router.post("/register", response_model=CreateUserReturn)
def api_register(user: User):
    """
    API endpoint to create a new user.

    This endpoint handles the creation of a new user by accepting a User object,
    processing it through the command bus, and returning the created user data.

    Args:
        user (User): The user object containing the details of the user to be created.

    Returns:
        CreateUserReturn: An object containing the data of the newly created user.
    """
    bus = bootstrap.bootstrap()
    cmd = commands.CreateUser(
        **user.dict(),
    )
    [new_user] = bus.handle(cmd)
    return CreateUserReturn(data=new_user)


@router.post("/login", response_model=OutputPostUserLoginReturn)
def api_login(user: InputPostUserLogin):
    """
    API endpoint to create a new user.

    This endpoint handles the creation of a new user by accepting a User object,
    processing it through the command bus, and returning the created user data.

    Args:
        user (User): The user object containing the details of the user to be created.

    Returns:
        CreateUserReturn: An object containing the data of the newly created user.
    """
    bus = bootstrap.bootstrap()
    cmd = commands.AuthenticateUser(
        **user.dict(),
    )
    [new_user] = bus.handle(cmd)
    return OutputPostUserLoginReturn(data=new_user)
