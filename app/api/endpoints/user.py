from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.user import User

user_router = APIRouter(prefix="/user")


@user_router.post("/")
def create_user(db: Session = Depends(get_db)):
    # TEST
    user = User(name="Someone", email="someone@gmail.com", password="12345")
    db.add(user)
    db.commit()
    db.refresh(user)

    return user
