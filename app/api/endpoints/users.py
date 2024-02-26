from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import UserCreateSchema, UserResponseSchema
from app.crud.user import get_user_by_email, create_user, get_user_by_id
from app.utils import generate_password_hash

user_router = APIRouter(prefix="/user")


@user_router.post("", response_model=UserResponseSchema)
def register_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    user.password = generate_password_hash(user.password)

    db_user = get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return create_user(db=db, user=user)


@user_router.get("/{id}", response_model=UserResponseSchema)
def get_user(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, id)

    if user is None:
        raise HTTPException(status_code=404, detail="User does not exist.")

    return user
