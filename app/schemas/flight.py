from datetime import datetime
from pydantic import BaseModel


class Flight(BaseModel):
    id: int
    name: str
    source: str
    destination: str
    departure: datetime
    reaching: datetime

    class Config:
        orm_mode = True
