from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import UserCreateSchema, UserResponseSchema
from app.schemas.ticket import TicketResponseSchema
from app.schemas.message import MessageSchema
from app.crud.user import get_user_by_email, create_user, get_user_by_id
from app.crud.ticket import get_ticket_by_user_id, delete_ticket
from app.auth.utils import generate_password_hash
from app.auth.dependencies import UserDep

user_router = APIRouter(prefix="/user")


@user_router.post("", response_model=UserResponseSchema)
async def register_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    user.password = generate_password_hash(user.password)

    db_user = get_user_by_email(db=db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return create_user(db=db, user=user)


@user_router.get("", response_model=UserResponseSchema)
async def get_user(user: UserDep, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=user.id)

    if user is None:
        raise HTTPException(status_code=404, detail="User does not exist.")

    return user


@user_router.get("/bookings", response_model=List[TicketResponseSchema])
async def get_bookings(user: UserDep, db: Session = Depends(get_db)):
    tickets = get_ticket_by_user_id(db, user_id=user.id)

    return tickets


@user_router.delete("/bookings/{id}", response_model=MessageSchema)
async def cancel_ticket(id: int, db: Session = Depends(get_db)):
    delete_ticket(db, ticket_id=id)

    return MessageSchema(message="Cancelled ticket successfully.")
