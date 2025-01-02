from fastapi import APIRouter, Depends
from app.modules.auth import bootstrap
from app.modules.auth.domain import commands
from app.modules.auth.domain.models import User
from app.infrastructure.api.schemas.user_schema import InputPostChangePassword
from app.shared.auth.role_checker import RoleChecker
from starlette.requests import Request

router = APIRouter()


@router.post(
    "/change_password",
)
def api_register(
    user: InputPostChangePassword,
    current_user=Depends(
        RoleChecker(
            allowed_roles=[
                "user",
            ],
        )
    ),
):
    """
    API endpoint to create a new user.

    This endpoint handles the creation of a new user by accepting a User object,
    processing it through the command bus, and returning the created user data.

    Args:
        user (User): The user object containing the details of the user to be created.

    Returns:
        CreateUserReturn: An object containing the data of the newly created user.
    """
    return {"response": "Create user"}
