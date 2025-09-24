from pydantic import BaseModel
from typing import Optional

class ConnectorBase(BaseModel):
    connector_id: str
    standard: str
    power_type: str
    max_voltage: int
    max_amperage: int
    tariff_id: Optional[str]

    def to_json(self) -> dict:
        return self.dict()
    

class ConnectorCreate(BaseModel):
    connector_id: str
    standard: str
    power_type: str
    max_voltage: float
    max_amperage: float
    tariff_id: Optional[str] = None

class ConnectorResponse(ConnectorBase):
    # Add DB fields if needed, e.g. created_at, updated_at
    class Config:
        orm_mode = True
