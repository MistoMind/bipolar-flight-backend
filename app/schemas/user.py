from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
