from pydantic import BaseModel


class TicketBookSchema(BaseModel):
    booked_seats: int
    flight_id: int
    user_id: int

    class Config:
        from_attributes = True


class TicketResponseSchema(TicketBookSchema):
    id: int

    class Config:
        from_attributes = True
