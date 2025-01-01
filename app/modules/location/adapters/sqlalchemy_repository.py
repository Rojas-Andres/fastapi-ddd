from sqlalchemy.orm import Session

from app.infrastructure.database.models import LocationORM
from app.modules.location.domain.repository import AbstractLocationRepository


class LocationSqlAlchemyRepository(AbstractLocationRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def get_locations(self) -> list[dict]:
        return [
            self.to_dict(location) for location in self.session.query(LocationORM).all()
        ]

    def create_location(self, name: str, latitude: float, longitude: float) -> dict:
        location = LocationORM(name=name, latitude=latitude, longitude=longitude)
        self.session.add(location)
        self.session.flush()
        return self.to_dict(location)

    def get_location_by_id(self, location_id: int) -> dict:
        location = self.session.query(LocationORM).filter_by(id=location_id).first()
        return self.to_dict(location) if location else None

    def to_dict(self, location: LocationORM) -> dict:
        return {
            "id": location.id,
            "name": location.name,
            "latitude": location.latitude,
            "longitude": location.longitude,
        }
