from fastapi import APIRouter
from app.modules.auth import bootstrap

router = APIRouter()


@router.post("/")
def api_create_user():
    bus = bootstrap.bootstrap()
    return {"data": "user created"}
    # categorys = services.GetAllCategorys(uow=CategoryUnitOfWork()).get()
    # return {"data": categorys}
