import logging
from typing import no_type_check
from app.modules.auth.domain import commands
from app.modules.auth.service_layer.unit_of_work import AbstractAuthUnitOfWork

logger = logging.getLogger(__name__)


def create_user(cmd: commands.CreateUser, uow: AbstractAuthUnitOfWork) -> str:
    logger.info("Create user handler")
    with uow:
        print("call command success")
        user_exist = uow.auth.get_by_email(email=cmd.email)
        if user_exist:
            raise ValueError("User already exists")
        print("User not exists")
