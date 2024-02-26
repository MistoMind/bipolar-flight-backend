from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreateSchema


def create_user(db: Session, user: UserCreateSchema):
    db_user = User(**user.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
