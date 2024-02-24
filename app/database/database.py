from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from constants import POSTGRES_URL


class Base(DeclarativeBase):
    pass


engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
