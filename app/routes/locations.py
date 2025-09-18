from fastapi import APIRouter
from app.models.location import LocationBase, Coordinates
from app.models.evse import EVSEBase
from app.models.connector import ConnectorBase
from app.utils.ocpi_response import ocpi_response

router = APIRouter(prefix="/ocpi/2.2", tags=["ocpi"])

@router.get("/locations")
def get_locations():
    loc = LocationBase(
        id="LOC-001",
        name="Berlin SuperCharger",
        address="Alexanderplatz 1",
        city="Berlin",
        country="DE",
        coordinates=Coordinates(latitude=52.5219, longitude=13.4132),
        evses=[
            EVSEBase(
                uid="EVSE-1",
                evse_id="DE*ABC*E001",
                status="AVAILABLE",
                connectors=[
                    ConnectorBase(
                        id="1",
                        standard="IEC_62196_T2",
                        power_type="AC_3_PHASE",
                        max_voltage=400,
                        max_amperage=32,
                        tariff_id="AC_STD"
                    )
                ]
            )
        ]
    )
    return ocpi_response([loc.to_json()])
