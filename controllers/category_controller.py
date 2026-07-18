from fastapi import APIRouter, HTTPException, status

from dtos.category.category_request_dto import CategoryRequestDTO
from dtos.category.category_response_dto import CategoryResponseDTO

from models.category import Category
from services.category_service import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Category"]
)

service = CategoryService()


@router.get("/", response_model=list[CategoryResponseDTO])
def find_all():

    return service.find_all()


@router.get("/{category_id}", response_model=CategoryResponseDTO)
def find_by_id(category_id: int):

    category = service.find_by_id(category_id)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found."
        )

    return category


@router.get("/search/{name}", response_model=list[CategoryResponseDTO])
def find_by_name(name: str):

    return service.find_by_name(name)


@router.get("/entity/{entity_id}", response_model=list[CategoryResponseDTO])
def find_by_entity(entity_id: int):

    return service.find_by_entity(entity_id)


@router.post(
    "/",
    response_model=CategoryResponseDTO,
    status_code=status.HTTP_201_CREATED
)
def create(dto: CategoryRequestDTO):

    category = Category(
        **dto.model_dump()
    )

    return service.create_category(category)


@router.put("/{category_id}", response_model=CategoryResponseDTO)
def update(category_id: int, dto: CategoryRequestDTO):

    category = service.update_category(
        category_id,
        **dto.model_dump(exclude_none=True)
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found."
        )

    return category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(category_id: int):

    deleted = service.delete_category(category_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found."
        )