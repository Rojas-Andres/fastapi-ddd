from app.modules.auth.adapters.sqlalchemy_repository import (
    UserSqlAlchemyRepository,
)

# from app.modules.auth.domain.repository import AbstractAuthRepository
from app.modules.auth.service_layer.unit_of_work import AbstractAuthUnitOfWork


class AuthUnitOfWork(AbstractAuthUnitOfWork):
    """
    A unit of work implementation for the Category module using SQLAlchemy.

    This class manages the lifecycle of a database session and provides a repository
    for performing operations on the Category entity.

    Methods:
        __enter__: Initializes the unit of work and sets up the category repository.
    """

    def __enter__(self):
        super().__enter__()
        self.user = UserSqlAlchemyRepository(self.session)
