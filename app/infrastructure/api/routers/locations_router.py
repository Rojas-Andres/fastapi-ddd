from fastapi import APIRouter

from app.modules.location.adapters.unit_of_work import LocationUnitOfWork
from app.modules.location.domain.models import LocationCreate
from app.modules.location.service_layer import services

router = APIRouter()


@router.get("/")
def api_get_locations():
    locations = services.GetAllLocations(uow=LocationUnitOfWork()).get()
    return {"data": locations}


@router.post("/")
def api_create_location(location_create: LocationCreate):
    location = services.CreateLocation(uow=LocationUnitOfWork()).create(
        **location_create.dict()
    )
    return {"data": location}


@router.get("/{location_id}")
def api_get_single_location(location_id: int):
    location = services.GetSingleLocation(uow=LocationUnitOfWork()).get(location_id)
    return {"data": location}
