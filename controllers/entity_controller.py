from datetime import datetime

from fastapi import APIRouter, HTTPException, status

from dtos.entity.entity_request_dto import EntityRequestDTO
from dtos.entity.entity_response_dto import EntityResponseDTO

from models.entity import Entity
from services.entity_service import EntityService

router = APIRouter(
    prefix="/entities",
    tags=["Entity"]
)

service = EntityService()


@router.get("/", response_model=list[EntityResponseDTO])
def find_all():

    entities = service.find_all()

    return entities


@router.get("/{entity_id}", response_model=EntityResponseDTO)
def find_by_id(entity_id: int):

    entity = service.find_by_id(entity_id)

    if entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Entity not found."
        )

    return entity


@router.get("/search/{name}", response_model=list[EntityResponseDTO])
def find_by_name(name: str):

    return service.find_by_name(name)


@router.post(
    "/",
    response_model=EntityResponseDTO,
    status_code=status.HTTP_201_CREATED
)
def create(dto: EntityRequestDTO):

    entity = Entity(
        **dto.model_dump(),
        created_at=datetime.now()
    )

    return service.create_entity(entity)


@router.put("/{entity_id}", response_model=EntityResponseDTO)
def update(entity_id: int, dto: EntityRequestDTO):

    entity = service.update_entity(
        entity_id,
        **dto.model_dump(exclude_none=True)
    )

    if entity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Entity not found."
        )

    return entity


@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(entity_id: int):

    deleted = service.delete_entity(entity_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Entity not found."
        )