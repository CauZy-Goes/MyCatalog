from pydantic import BaseModel

from dtos.entity.entity_response_dto import EntityResponseDTO


class CategoryResponseDTO(BaseModel):
    id: int | None = None
    name: str | None = None
    order: int | None = None

    entity: EntityResponseDTO | None = None