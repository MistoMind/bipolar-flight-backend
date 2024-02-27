from pydantic import BaseModel, EmailStr


class AdminDBSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class AdminCreateSchema(AdminDBSchema):
    admin_create_key: str

    class Config:
        from_attributes = True


class AdminResponseSchema(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
