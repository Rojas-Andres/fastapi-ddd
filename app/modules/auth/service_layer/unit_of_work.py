from app.modules.auth.domain.repository import (
    AbstractUserRepository,
)
from app.domain.base_domain.service_layer.unit_of_work import SqlAlchemyUnitOfWork


class AbstractAuthUnitOfWork(SqlAlchemyUnitOfWork):
    user: AbstractUserRepository
