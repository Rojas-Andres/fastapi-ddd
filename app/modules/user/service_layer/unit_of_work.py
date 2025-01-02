from app.modules.user.domain.repository import (
    AbstractUserRepository,
)
from app.domain.base_domain.service_layer.unit_of_work import SqlAlchemyUnitOfWork


class AbstractUserUnitOfWork(SqlAlchemyUnitOfWork):
    user: AbstractUserRepository
