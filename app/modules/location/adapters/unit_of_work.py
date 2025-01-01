from app.modules.location.adapters.sqlalchemy_repository import (
    LocationSqlAlchemyRepository,
)
from app.modules.location.domain.repository import AbstractLocationUnitOfWork


class LocationUnitOfWork(AbstractLocationUnitOfWork):
    def __enter__(self):
        super().__enter__()
        self.location = LocationSqlAlchemyRepository(self.session)
