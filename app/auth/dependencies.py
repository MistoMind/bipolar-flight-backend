from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.config import settings
from app.crud.user import get_user_by_email
from app.crud.admin import get_admin_by_email
from app.database.dependencies import get_db
from app.schemas.token import TokenDataSchema
from app.schemas.user import UserResponseSchema
from app.schemas.admin import AdminResponseSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/user/login")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception

        token_data = TokenDataSchema(email=email)
    except JWTError:
        raise credentials_exception

    user = get_user_by_email(db=db, email=token_data.email)

    if user is None:
        raise credentials_exception

    return user


async def get_admin(
    token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception

        token_data = TokenDataSchema(email=email)
    except JWTError:
        raise credentials_exception

    admin = get_admin_by_email(db=db, email=token_data.email)

    if admin is None:
        raise credentials_exception

    return admin


UserDep = Annotated[UserResponseSchema, Depends(get_current_user)]
AdminDep = Annotated[AdminResponseSchema, Depends(get_admin)]
