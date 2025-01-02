from fastapi import APIRouter, Depends
from app.modules.user import bootstrap
from app.modules.user.domain import commands
from app.modules.auth.domain.models import User
from app.infrastructure.api.schemas.user_schema import InputPostChangePassword
from app.shared.auth.role_checker import RoleChecker
from starlette.requests import Request

router = APIRouter()


@router.post(
    "/change_password",
)
def api_change_password(
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
    bus = bootstrap.bootstrap()
    cmd = commands.ChangePasswordUser(
        **user.dict(),
        user_id=current_user.user_id,
    )
    [_] = bus.handle(cmd)
    return {"response": "Change password success"}
