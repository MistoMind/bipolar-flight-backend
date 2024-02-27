from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.schemas.ticket import TicketBookSchema


def create_ticket(db: Session, ticket: TicketBookSchema):
    db_ticket = Ticket(**ticket.model_dump())

    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)

    return db_ticket
