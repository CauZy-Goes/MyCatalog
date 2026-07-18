from pydantic import BaseModel, EmailStr


class CategoryRequestDTO(BaseModel):
    name: str | None = None
    entity_id: int | None = None
    order: int | None = None