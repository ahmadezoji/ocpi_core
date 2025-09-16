from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/ocpi", tags=["ocpi"])

class Version(BaseModel):
    version: str
    url: str

@router.get("/versions", response_model=List[Version])
async def get_versions():
    # Static example per OCPI spec; normally discovered at /ocpi/versions
    return [
        Version(version="2.2.1", url="/ocpi/2.2.1"),
        Version(version="2.2", url="/ocpi/2.2"),
    ]
