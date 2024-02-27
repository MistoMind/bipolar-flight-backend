from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.flight import Flight
from app.schemas.message import MessageSchema
from app.schemas.flight import (
    FlightCreateSchema,
    FlightResponseSchema,
    FlightSearchSchema,
)
from app.schemas.ticket import TicketBookSchema, TicketResponseSchema
from app.crud.flight import (
    get_flight_by_name,
    create_flight,
    delete_flight,
    get_flight_by_id,
    filter_flights,
    reserve_available_seats,
)
from app.crud.user import get_user_by_id
from app.crud.ticket import create_ticket

flight_router = APIRouter(prefix="/flight")


@flight_router.post("", response_model=FlightResponseSchema)
def register_flight(flight: FlightCreateSchema, db: Session = Depends(get_db)):
    db_flight = get_flight_by_name(db=db, name=flight.name)

    if db_flight:
        raise HTTPException(status_code=400, detail="Flight already registered")

    return create_flight(db=db, flight=flight)


@flight_router.delete("/{id}", response_model=MessageSchema)
def remove_flight(id: int, db: Session = Depends(get_db)):
    count = delete_flight(db=db, flight_id=id)

    if count == 0:
        raise HTTPException(status_code=404, detail="Flight does not exist.")

    return MessageSchema(message="Flight Removed successfully.")


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


@flight_router.post("/book", response_model=TicketResponseSchema)
def book_flight(ticket: TicketBookSchema, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=ticket.user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User does not exist.")

    flight = get_flight_by_id(db=db, flight_id=ticket.flight_id)

    if flight is None:
        raise HTTPException(status_code=404, detail="Flight does not exist.")

    count = reserve_available_seats(
        db=db, flight_id=ticket.flight_id, reserve_seats=ticket.booked_seats
    )

    if count == 0:
        raise HTTPException(status_code=400, detail="Seats are full.")

    return create_ticket(db=db, ticket=ticket)
