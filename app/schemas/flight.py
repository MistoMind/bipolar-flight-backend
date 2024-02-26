from datetime import date, time
from pydantic import BaseModel


class FlightCreateSchema(BaseModel):
    name: str
    source: str
    destination: str
    dep_date: date
    departure: time
    arrival: time
    price: float
    total_seats: int = 60
    available_seats: int | None = 60

    class Config:
        from_attributes = True


class FlightResponseSchema(FlightCreateSchema):
    id: int

    class Config:
        from_attributes = True


class FlightSearchSchema(BaseModel):
    source: str
    destination: str
    dep_date: date

    class Config:
        from_attributes = True
