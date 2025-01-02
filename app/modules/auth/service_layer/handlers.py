import logging
from app.modules.auth.domain import commands, events
from app.modules.auth.service_layer.unit_of_work import AbstractAuthUnitOfWork
from app.modules.auth.domain import models
from app.shared.auth.auth_class import HasherAbstract, TokenHandler
from app.infrastructure.api.schemas.auth_schema import (
    UserCreateReturn,
    OutputPostUserLogin,
)
from datetime import timedelta, datetime

from app.core.config import settings

logger = logging.getLogger(__name__)


def create_user(
    cmd: commands.CreateUser, uow: AbstractAuthUnitOfWork, hasher: HasherAbstract
) -> str:
    logger.info("Create user handler")
    with uow:
        user_exist = uow.user.get_by_email(email=cmd.email)
        if user_exist:
            raise ValueError("User already exists")
        hashed_password = hasher.get_password_hash(cmd.password)
        user = uow.user.create(
            models.User(
                email=cmd.email,
                password=hashed_password,
                first_name=cmd.first_name,
                last_name=cmd.last_name,
            )
        )
        uow.commit()
        user_id = user.id
    uow.add_event(events.UserCreated(user_id=user_id))
    return UserCreateReturn(
        id=user_id,
        email=user.email,
        first_name=user.first_name,
        last_name=cmd.last_name,
    )


def login_user(
    cmd: commands.AuthenticateUser,
    uow: AbstractAuthUnitOfWork,
    hasher: HasherAbstract,
    token_handler: TokenHandler,
) -> str:
    logger.info("Login user handler")
    with uow:
        user = uow.user.get_by_email(email=cmd.email)
        if not user:
            raise ValueError("User not found")
        if not hasher.verify_password(cmd.password, user.password):
            raise ValueError("Invalid password")
    to_expiration = timedelta(minutes=settings.COMMAND_TOKEN_MINUTES_EXPIRATION)
    expires = datetime.now() + to_expiration
    token_value: str = token_handler.encode(
        payload={
            "user_id": user.id,
        },
        expires=expires,
    )
    return OutputPostUserLogin(
        jwt=token_value,
    )


def new_user_notification(
    event: events.NewUserNotification,
    uow: AbstractAuthUnitOfWork,
):
    logger.info("New user notification")
    with uow:
        user = uow.user.get_by_id(user_id=event.user_id)
        print("this is a user", user)
        if not user:
            raise ValueError("User not found")

    print(f"New user notification sent to {user.email}")
    logger.info("New user notification sent")
