from app.core.exceptions import ObjectNotFoundException
from app.modules.location.domain.repository import AbstractLocationUnitOfWork


class GetAllLocations:
    def __init__(
        self,
        uow: AbstractLocationUnitOfWork,
    ):
        self.uow = uow

    def get(self):
        with self.uow:
            locations = self.uow.location.get_locations()
            return locations


class CreateLocation:
    def __init__(
        self,
        uow: AbstractLocationUnitOfWork,
    ):
        self.uow = uow

    def create(self, name: str, latitude: float, longitude: float):
        with self.uow:
            new_location = self.uow.location.create_location(
                name=name, latitude=latitude, longitude=longitude
            )
            self.uow.commit()
            return new_location


class GetSingleLocation:
    def __init__(
        self,
        uow: AbstractLocationUnitOfWork,
    ):
        self.uow = uow

    def get(self, location_id: int):
        with self.uow:
            location = self.uow.location.get_location_by_id(location_id)
            if not location:
                raise ObjectNotFoundException("Location not found")
            return location
