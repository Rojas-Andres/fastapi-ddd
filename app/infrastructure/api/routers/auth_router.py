from fastapi import APIRouter
from app.modules.auth import bootstrap
from app.modules.auth.domain import commands
from app.modules.auth.domain.models import User

router = APIRouter()


@router.post("/")
def api_create_user(user: User):
    bus = bootstrap.bootstrap()
    cmd = commands.CreateUser(
        **user.dict(),
    )
    [user_] = bus.handle(cmd)
    return {"data": "user created"}
