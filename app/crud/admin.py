from sqlalchemy.orm import Session

from app.models.admin import Admin
from app.schemas.admin import AdminDBSchema


def create_admin(db: Session, admin: AdminDBSchema):
    db_admin = Admin(**admin.model_dump())

    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)

    return db_admin


def get_admin_by_email(db: Session, email: str):
    return db.query(Admin).filter(Admin.email == email).first()
