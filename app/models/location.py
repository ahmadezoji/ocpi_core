from pydantic import BaseModel
from typing import List
from app.models.evse import EVSEBase

class Coordinates(BaseModel):
    latitude: float
    longitude: float

class LocationBase(BaseModel):
    id: str
    name: str
    address: str
    city: str
    country: str
    coordinates: Coordinates
    evses: List[EVSEBase]

    def to_json(self) -> dict:
        data = self.dict(exclude={"coordinates", "evses"})
        data["latitude"] = self.coordinates.latitude
        data["longitude"] = self.coordinates.longitude
        data["evses"] = [evse.to_json() for evse in self.evses]
        return data

class LocationCreate(LocationBase):
    pass

class LocationResponse(LocationBase):
    # Add DB fields if needed, e.g. created_at, updated_at
    class Config:
        orm_mode = True
