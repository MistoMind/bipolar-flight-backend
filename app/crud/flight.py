from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.flight import Flight
from app.schemas.flight import FlightCreateSchema


def create_flight(db: Session, flight: FlightCreateSchema):
    db_flight = Flight(**flight.model_dump())

    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)

    return db_flight


def delete_flight(db: Session, flight_id: int):
    flight = get_flight_by_id(db=db, flight_id=flight_id)

    if flight is None:
        raise HTTPException(status_code=404, detail="Flight does not exist.")

    db.query(Flight).filter(Flight.id == flight_id).delete()
    db.commit()


def get_flight_by_id(db: Session, flight_id: int):
    return db.query(Flight).filter(Flight.id == flight_id).first()


def get_flight_by_name(db: Session, name: str):
    return db.query(Flight).filter(Flight.name == name).first()


def get_all_flights(db: Session):
    return db.query(Flight).all()


def filter_flights(db: Session, *criteria):
    return db.query(Flight).filter(*criteria).all()


def reserve_available_seats(db: Session, flight_id: int, reserve_seats: int):
    flight = get_flight_by_id(db=db, flight_id=flight_id)

    if flight.available_seats - reserve_seats >= 0:
        db.query(Flight).filter(Flight.id == flight_id).update(
            {Flight.available_seats: Flight.available_seats - reserve_seats}
        )

        db.commit()
    else:
        raise HTTPException(status_code=400, detail="Not enough seats available.")
