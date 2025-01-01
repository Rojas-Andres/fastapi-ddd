from app.domain.authentication.adapters.repository import (
    AbstractGroupRepository,
    AbstractUserRepository,
)
from app.domain.base_domain.service_layer.unit_of_work import AbstractUnitOfWork


class AbstractAuthUnitOfWork(AbstractUnitOfWork):
    users: AbstractUserRepository
    groups: AbstractGroupRepository
