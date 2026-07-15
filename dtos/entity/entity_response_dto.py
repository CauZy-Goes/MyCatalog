from datetime import datetime

from pydantic import BaseModel, EmailStr


class EntityResponseDTO(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime | None = None
    address: str | None = None
    email: EmailStr | None = None
    phoneNumber: int | None = None