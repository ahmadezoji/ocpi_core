from fastapi import APIRouter
from app.utils.ocpi_response import ocpi_response
from app.settings import BACKEND_HOST,OCPI_CORE_PORT
from app.utils.logger import Logger

router = APIRouter(prefix="/ocpi/2.2", tags=["ocpi"])
logger = Logger("ocpi_core.credentials_route").get_logger()

@router.get("/credentials")
def get_credentials():
    logger.info("Serving OCPI credentials")
    return ocpi_response({
        "token": "CPO_TOKEN_123",
        "url": f"http://{BACKEND_HOST}:{OCPI_CORE_PORT}/ocpi/versions",
        "business_details": {"name": "MyCPO", "website": "https://mycpo.com"},
        "country_code": "DE",
        "party_id": "CPO1"
    })
