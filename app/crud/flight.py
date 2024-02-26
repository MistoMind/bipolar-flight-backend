from sqlalchemy.orm import Session

from app.models.flight import Flight
from app.schemas.flight import FlightCreateSchema


def create_flight(db: Session, flight: FlightCreateSchema):
    db_flight = Flight(**flight.model_dump())

    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)

    return db_flight


def get_flight_by_id(db: Session, flight_id: int):
    return db.query(Flight).filter(Flight.id == flight_id).first()


def get_flight_by_name(db: Session, name: str):
    return db.query(Flight).filter(Flight.name == name).first()


def get_all_flights(db: Session):
    return db.query(Flight).all()


def filter_flights(db: Session, *criteria):
    return db.query(Flight).filter(*criteria).all()


def reserve_available_seats(db: Session, flight_id: int, reserve_seats: int):
    db.query(Flight).filter(Flight.id == flight_id).update(
        {Flight.available_seats: Flight.available_seats - reserve_seats}
    )
    db.commit()
