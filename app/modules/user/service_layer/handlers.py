import logging
from app.modules.user.domain import commands
from app.modules.user.service_layer.unit_of_work import AbstractUserUnitOfWork
from app.shared.auth.auth_class import HasherAbstract


logger = logging.getLogger(__name__)


def change_password_user(
    cmd: commands.ChangePasswordUser,
    uow: AbstractUserUnitOfWork,
    hasher: HasherAbstract,
) -> str:
    logger.info("Create user handler")
    with uow:
        user = uow.user.get_by_id(user_id=cmd.user_id)
        if not user:
            raise ValueError("User not found")
        if not hasher.verify_password(
            plain_password=cmd.current_password, hashed_password=user.password
        ):
            raise ValueError("Password not match")
        uow.user.change_password(
            user_id=cmd.user_id, new_password=hasher.get_password_hash(cmd.new_password)
        )
        uow.commit()
