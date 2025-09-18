from fastapi import APIRouter
from app.utils.ocpi_response import ocpi_response  # Assumes you have this utility
from app.settings import BACKEND_HOST,OCPI_CORE_PORT
router = APIRouter(prefix="/ocpi/2.2", tags=["ocpi"])

@router.get("/credentials")
def get_credentials():
    return ocpi_response({
        "token": "CPO_TOKEN_123",
        "url": f"http://{BACKEND_HOST}:{OCPI_CORE_PORT}/ocpi/versions",
        "business_details": {"name": "MyCPO", "website": "https://mycpo.com"},
        "country_code": "DE",
        "party_id": "CPO1"
    })
