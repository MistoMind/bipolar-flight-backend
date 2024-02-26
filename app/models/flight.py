from datetime import date, time
from sqlalchemy import Integer, String, Date, Time, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Flight(Base):
    __tablename__ = "flight"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    source: Mapped[str] = mapped_column(String)
    destination: Mapped[str] = mapped_column(String)
    dep_date: Mapped[date] = mapped_column(Date)
    departure: Mapped[time] = mapped_column(Time)
    arrival: Mapped[time] = mapped_column(Time)
    price: Mapped[float] = mapped_column(Float)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.password!r})"
