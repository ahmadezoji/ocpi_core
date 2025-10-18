from fastapi import HTTPException
import httpx

from app.settings import BACKEND_HOST,BACKEND_PORT
from app.utils.logger import Logger

BASE_URL = f"http://127.0.0.1:{BACKEND_PORT}"
logger = Logger("ocpi_core.charge_point_repository").get_logger()

class ChargePointRepository:
    async def fetch_charge_points(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{BASE_URL}/charge_points/")
                response.raise_for_status()
                logger.info("Fetched charge points successfully")
                return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Failed to fetch charge points: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to fetch charge points: {str(e)}")

