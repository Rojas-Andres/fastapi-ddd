import logging
from app.modules.auth.domain import commands, events
from app.modules.auth.service_layer.unit_of_work import AbstractAuthUnitOfWork
from app.modules.auth.domain import models
from sqlalchemy import text

logger = logging.getLogger(__name__)


def create_user(cmd: commands.CreateUser, uow: AbstractAuthUnitOfWork) -> str:
    logger.info("Create user handler")
    with uow:
        print("call command success")
        user_exist = uow.user.get_by_email(email=cmd.email)
        if user_exist:
            raise ValueError("User already exists")
        user = uow.user.create(
            models.User(
                email=cmd.email,
                password=cmd.password,
                first_name=cmd.first_name,
                last_name=cmd.last_name,
            )
        )
        uow.commit()
        user_id = user.id
        print("User not exists")
    uow.add_event(events.UserCreated(user_id=user_id))


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
