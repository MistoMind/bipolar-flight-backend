from datetime import date, time
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Flight(Base):
    __tablename__ = "flight"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    source: Mapped[str] = mapped_column()
    destination: Mapped[str] = mapped_column()
    dep_date: Mapped[date] = mapped_column()
    departure: Mapped[time] = mapped_column()
    arrival: Mapped[time] = mapped_column()
    price: Mapped[float] = mapped_column()
    total_seats: Mapped[int] = mapped_column(default=60)
    available_seats: Mapped[int] = mapped_column(default=60)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.password!r})"
