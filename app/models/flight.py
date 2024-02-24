from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Flight(Base):
    __tablename__ = "flight"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    source: Mapped[str] = mapped_column(String)
    destination: Mapped[str] = mapped_column(String)
    departure: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    reaching: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.password!r})"
