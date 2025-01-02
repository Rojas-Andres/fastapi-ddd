from app.modules.user.adapters.sqlalchemy_repository import (
    UserSqlAlchemyRepository,
)

from app.modules.user.service_layer.unit_of_work import AbstractUserUnitOfWork


class UserUnitOfWork(AbstractUserUnitOfWork):
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
