from datetime import datetime
from pydantic import BaseModel


class FlightCreateSchema(BaseModel):
    name: str
    source: str
    destination: str
    departure: datetime
    reaching: datetime

    class Config:
        from_attributes = True


class FlightResponseSchema(FlightCreateSchema):
    id: int

    class Config:
        from_attributes = True


class FlightSearchSchema(BaseModel):
    source: str
    destination: str

    class Config:
        from_attributes = True
