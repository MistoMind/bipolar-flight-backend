from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import UserCreateSchema, UserResponseSchema
from app.crud.user import get_user_by_email, create_user


user_router = APIRouter(prefix="/user")


@user_router.post("/", response_model=UserResponseSchema)
def register_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return create_user(db=db, user=user)
