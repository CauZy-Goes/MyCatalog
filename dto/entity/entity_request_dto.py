from pydantic import BaseModel, EmailStr


class EntityUpdateDTO(BaseModel):
    name: str | None = None
    description: str | None = None
    address: str | None = None
    email: EmailStr | None = None
    phoneNumber: int | None = None