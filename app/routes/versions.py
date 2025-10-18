from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.utils.logger import Logger

router = APIRouter(prefix="/ocpi", tags=["ocpi"])
logger = Logger("ocpi_core.versions_route").get_logger()

class Version(BaseModel):
    version: str
    url: str

@router.get("/versions", response_model=List[Version])
async def get_versions():
    logger.info("Serving OCPI versions")
    # Static example per OCPI spec; normally discovered at /ocpi/versions
    return [
        Version(version="2.2.1", url="/ocpi/2.2.1"),
        Version(version="2.2", url="/ocpi/2.2"),
    ]
