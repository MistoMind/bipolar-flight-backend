from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, Session

from app.database import Base
from app.schemas.user import UserCreateSchema


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String(30))

    @classmethod
    def create_user(cls, db: Session, user: UserCreateSchema):
        db_user = User(**user.model_dump())

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @classmethod
    def get_user(cls, db: Session, user_id: int):
        return db.query(cls).filter(cls.id == user_id).first()

    @classmethod
    def get_user_by_email(cls, db: Session, email: str):
        return db.query(cls).filter(cls.email == email).first()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"
