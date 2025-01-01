from fastapi import APIRouter
from app.modules.auth import bootstrap
from app.modules.auth.domain import commands
router = APIRouter()


@router.post("/")
def api_create_user():
    bus = bootstrap.bootstrap()
    cmd = commands.CreateUser(
        email="aaaa",
        password="new_password",
    )
    [user_] = bus.handle(cmd)
    return {"data": "user created"}
    # categorys = services.GetAllCategorys(uow=CategoryUnitOfWork()).get()
    # return {"data": categorys}
