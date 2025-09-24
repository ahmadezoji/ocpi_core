from fastapi import APIRouter
from app.models.location import LocationBase, Coordinates
from app.models.evse import EVSEBase  # <-- import EVSEBase
from app.repositories.charge_point_repository import ChargePointRepository
from app.utils.ocpi_response import ocpi_response

router = APIRouter(prefix="/ocpi/2.2", tags=["ocpi"])

repo = ChargePointRepository()


@router.get("/locations")
async def get_locations():
    charge_points = await repo.fetch_charge_points()
    locations = []
    if len(charge_points) == 0 or "error" in charge_points:
        return None
    for cp in charge_points:
        # Build EVSEs from charge point data
        evse = EVSEBase(
            uid=cp["charge_point_id"],
            evse_id=cp["charge_point_id"],
            status="AVAILABLE",  # or map from cp if available
            connectors=cp["connectors"]
        )
        loc = LocationBase(
            id=cp["charge_point_id"],
            name=cp["name"],
            address=cp["address"],
            city=cp["city"],
            country=cp["country"],
            coordinates=Coordinates(
                latitude=cp.get("latitude", None),
                longitude=cp.get("longitude",None)
            ),
            evses=[evse.to_json()]
        )
        locations.append(loc.to_json())
    return ocpi_response(locations)
