from datetime import timedelta, datetime, timezone
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config import settings
from app.crud.user import get_user_by_email
from app.crud.admin import get_admin_by_email

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def generate_password_hash(password: str):
    return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db=db, email=email)

    if not user:
        return False

    if not verify_password(password, user.password):
        return False

    return user


def authenticate_admin(db: Session, email: str, password: str):
    admin = get_admin_by_email(db=db, email=email)

    if not admin:
        return False

    if not verify_password(password, admin.password):
        return False

    return admin


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.algorithm
    )

    return encoded_jwt
