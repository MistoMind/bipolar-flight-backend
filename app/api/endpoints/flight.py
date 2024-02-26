from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.flight import (
    FlightCreateSchema,
    FlightResponseSchema,
    FlightSearchSchema,
)
from app.crud.flight import (
    get_flight_by_name,
    create_flight,
    get_flight_by_id,
    get_all_flights,
)

flight_router = APIRouter(prefix="/flight")


@flight_router.post("", response_model=FlightResponseSchema)
def register_flight(flight: FlightCreateSchema, db: Session = Depends(get_db)):
    db_flight = get_flight_by_name(db, name=flight.name)

    if db_flight:
        raise HTTPException(status_code=400, detail="Flight already registered")

    return create_flight(db=db, flight=flight)


@flight_router.get("/{id}", response_model=FlightResponseSchema)
def get_flight(id: int, db: Session = Depends(get_db)):
    flight = get_flight_by_id(db, id)

    if flight is None:
        raise HTTPException(status_code=404, detail="Flight does not exist.")

    return flight


@flight_router.post("/search", response_model=List[FlightResponseSchema])
def search_flights(query: FlightSearchSchema, db: Session = Depends(get_db)):
    all_flights = get_all_flights(db)
    result_flights = []

    for flight in all_flights:
        if flight.source == query.source and flight.destination == query.destination:
            result_flights.append(flight)

    return result_flights
