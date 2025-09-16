from pydantic import BaseModel
from typing import List
from app.models.connector import ConnectorBase

class EVSEBase(BaseModel):
    uid: str
    evse_id: str
    status: str
    connectors: List[ConnectorBase]

    def to_json(self) -> dict:
        data = self.dict(exclude={"connectors"})
        data["connectors"] = [connector.to_json() for connector in self.connectors]
        return data

class EVSECreate(EVSEBase):
    pass

class EVSEResponse(EVSEBase):
    # Add DB fields if needed, e.g. created_at, updated_at
    class Config:
        orm_mode = True
