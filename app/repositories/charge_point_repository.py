from fastapi import HTTPException
import httpx

from app.settings import BACKEND_HOST,BACKEND_PORT

BASE_URL = f"http://127.0.0.1:{BACKEND_PORT}"

class ChargePointRepository:
    async def fetch_charge_points(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{BASE_URL}/charge_points/")
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Failed to fetch charge points: {str(e)}")

