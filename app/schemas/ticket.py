from pydantic import BaseModel


class TicketBookSchema(BaseModel):
    booked_seats: int
    flight_id: int

    class Config:
        from_attributes = True


class TicketSchema(TicketBookSchema):
    user_id: int

    class Config:
        from_attributes = True


class TicketResponseSchema(TicketSchema):
    id: int

    class Config:
        from_attributes = True
