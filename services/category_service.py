from sqlalchemy import func, select

from config.database.database import SessionLocal
from models.category import Category


class CategoryService:

    def __init__(self):
        self.db = SessionLocal()

    def find_all(self) -> list[Category]:
        stmt = select(Category)
        return list(self.db.scalars(stmt).all())

    def find_by_id(self, category_id: int) -> Category | None:
        stmt = select(Category).where(Category.id == category_id)
        return self.db.scalar(stmt)

    def find_by_name(self, text: str) -> list[Category]:
        stmt = select(Category).where(Category.name.contains(text))
        return list(self.db.scalars(stmt).all())

    def find_by_entity(self, entity_id: int) -> list[Category]:
        stmt = select(Category).where(Category.entity_id == entity_id)
        return list(self.db.scalars(stmt).all())

    def create_category(self, category: Category) -> Category:
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category

    def update_category(self, category_id: int, **kwargs) -> Category | None:
        category = self.find_by_id(category_id)

        if category is None:
            return None

        for key, value in kwargs.items():
            if hasattr(category, key):
                setattr(category, key, value)

        self.db.commit()
        self.db.refresh(category)

        return category

    def delete_category(self, category_id: int) -> bool:
        category = self.find_by_id(category_id)

        if category is None:
            return False

        self.db.delete(category)
        self.db.commit()

        return True
    
    def _get_last_order(self, entity_id: int) -> int:
        """
        Retorna o maior order existente para a entidade.

        Exemplo:

            Entity 1
            --------
            Order: 1
            Order: 2
            Order: 3

            Retorno:
                3

        Caso a entidade ainda não possua categorias,
        retorna 0.
        """

        stmt = (
            select(func.max(Category.order))
            .where(Category.entity_id == entity_id)
        )

        return self.db.scalar(stmt) or 0
