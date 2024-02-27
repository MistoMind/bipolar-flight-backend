from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.admin import AdminResponseSchema, AdminCreateSchema, AdminDBSchema
from app.database.dependencies import get_db
from app.crud.admin import create_admin, get_admin_by_email
from app.config import settings
from app.auth.utils import generate_password_hash

admin_router = APIRouter(prefix="/admin")


@admin_router.post("", response_model=AdminResponseSchema)
async def register_admin(
    admin_details: AdminCreateSchema, db: Session = Depends(get_db)
):
    if admin_details.admin_create_key != settings.admin_create_key:
        raise HTTPException(status_code=400, detail="Wrong admin create key.")

    admin_details.password = generate_password_hash(admin_details.password)

    db_user = get_admin_by_email(db=db, email=admin_details.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    admin = AdminDBSchema(
        name=admin_details.name,
        email=admin_details.email,
        password=admin_details.password,
    )

    return create_admin(db=db, admin=admin)
