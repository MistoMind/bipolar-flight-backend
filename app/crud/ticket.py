from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.schemas.ticket import TicketBookSchema


def create_ticket(db: Session, ticket: TicketBookSchema):
    db_ticket = Ticket(**ticket.model_dump())

    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)

    return db_ticket


def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter_by(id=ticket_id).first()


def get_ticket_by_user_id(db: Session, user_id: int):
    return db.query(Ticket).filter_by(user_id=user_id).all()


def delete_ticket(db: Session, ticket_id: int):
    ticket = get_ticket_by_id(db=db, ticket_id=ticket_id)

    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket does not exist.")

    db.query(Ticket).filter_by(id=ticket_id).delete()
    db.commit()
