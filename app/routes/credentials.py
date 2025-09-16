from fastapi import APIRouter
from app.utils.ocpi_response import ocpi_response  # Assumes you have this utility
from app.config import BACKEND_HOST, OCPI_PORT  # Assumes these are defined somewhere

router = APIRouter(prefix="/ocpi/2.2", tags=["ocpi"])

@router.get("/credentials")
def get_credentials():
    return ocpi_response({
        "token": "CPO_TOKEN_123",
        "url": f"http://{BACKEND_HOST}:{OCPI_PORT}/ocpi/versions",
        "business_details": {"name": "MyCPO", "website": "https://mycpo.com"},
        "country_code": "DE",
        "party_id": "CPO1"
    })
