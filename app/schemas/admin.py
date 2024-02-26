from pydantic import BaseModel, EmailStr


class Admin(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True
