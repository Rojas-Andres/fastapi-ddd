from abc import ABC, abstractmethod

from app.modules.shared.domain.repository import SqlAlchemyUnitOfWork


class AbstractLocationRepository(ABC):
    @abstractmethod
    def get_locations(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def create_location(self, name: str, latitude: float, longitude: float) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_location_by_id(self, location_id: int) -> dict:
        raise NotImplementedError


class AbstractLocationUnitOfWork(SqlAlchemyUnitOfWork):
    location: AbstractLocationRepository

    def __enter__(self):
        self.session = self.session_factory()  # noqa
        return super().__enter__()
