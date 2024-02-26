from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.flight import Flight
from app.schemas.flight import (
    FlightCreateSchema,
    FlightResponseSchema,
    FlightSearchSchema,
)
from app.crud.flight import (
    get_flight_by_name,
    create_flight,
    get_flight_by_id,
    filter_flights,
)

flight_router = APIRouter(prefix="/flight")


@flight_router.post("", response_model=FlightResponseSchema)
def register_flight(flight: FlightCreateSchema, db: Session = Depends(get_db)):
    db_flight = get_flight_by_name(db=db, name=flight.name)

    if db_flight:
        raise HTTPException(status_code=400, detail="Flight already registered")

    return create_flight(db=db, flight=flight)


@flight_router.get("/{id}", response_model=FlightResponseSchema)
def get_flight(id: int, db: Session = Depends(get_db)):
    flight = get_flight_by_id(db=db, flight_id=id)

    if flight is None:
        raise HTTPException(status_code=404, detail="Flight does not exist.")

    return flight


@flight_router.post("/search", response_model=List[FlightResponseSchema])
def search_flights(query: FlightSearchSchema, db: Session = Depends(get_db)):
    filtered_flights = filter_flights(
        db,
        Flight.source == query.source,
        Flight.destination == query.destination,
        Flight.dep_date == query.dep_date,
    )

    return filtered_flights
