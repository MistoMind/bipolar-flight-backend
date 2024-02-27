from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.auth.dependencies import UserDep
from app.auth.dependencies import AdminDep
from app.models.flight import Flight
from app.schemas.message import MessageSchema
from app.schemas.flight import (
    FlightCreateSchema,
    FlightResponseSchema,
    FlightSearchSchema,
)
from app.schemas.ticket import TicketBookSchema, TicketResponseSchema, TicketSchema
from app.crud.flight import (
    get_flight_by_name,
    create_flight,
    delete_flight,
    get_flight_by_id,
    filter_flights,
    reserve_available_seats,
)
from app.crud.user import get_user_by_id
from app.crud.ticket import create_ticket, get_ticket_by_flight_id, delete_ticket

flight_router = APIRouter(prefix="/flight")


@flight_router.post("", response_model=FlightResponseSchema)
async def register_flight(
    admin: AdminDep, flight: FlightCreateSchema, db: Session = Depends(get_db)
):
    db_flight = get_flight_by_name(db=db, name=flight.name)

    if db_flight:
        raise HTTPException(status_code=400, detail="Flight already registered")

    return create_flight(db=db, flight=flight)


@flight_router.delete("/{id}", response_model=MessageSchema)
async def remove_flight(admin: AdminDep, id: int, db: Session = Depends(get_db)):
    tickets = get_ticket_by_flight_id(db=db, flight_id=id)

    for ticket in tickets:
        delete_ticket(db=db, ticket_id=ticket.id)

    delete_flight(db=db, flight_id=id)

    return MessageSchema(message="Flight Removed successfully.")


@flight_router.post("/search", response_model=List[FlightResponseSchema])
async def search_flights(query: FlightSearchSchema, db: Session = Depends(get_db)):
    filtered_flights = filter_flights(
        db,
        Flight.source == query.source,
        Flight.destination == query.destination,
        Flight.dep_date == query.dep_date,
    )

    return filtered_flights


@flight_router.post("/book", response_model=TicketResponseSchema)
async def book_flight(
    user: UserDep, booking_info: TicketBookSchema, db: Session = Depends(get_db)
):
    user = get_user_by_id(db=db, user_id=user.id)

    if user is None:
        raise HTTPException(status_code=404, detail="User does not exist.")

    flight = get_flight_by_id(db=db, flight_id=booking_info.flight_id)

    if flight is None:
        raise HTTPException(status_code=404, detail="Flight does not exist.")

    reserve_available_seats(
        db=db, flight_id=booking_info.flight_id, reserve_seats=booking_info.booked_seats
    )

    new_ticket = TicketSchema(
        booked_seats=booking_info.booked_seats,
        flight_id=booking_info.flight_id,
        user_id=user.id,
    )

    return create_ticket(db=db, ticket=new_ticket)
