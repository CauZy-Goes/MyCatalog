from sqlalchemy import select

from config.database.database import SessionLocal
from models.category_item import CategoryItem


class CategoryItemService:

    def __init__(self):
        self.db = SessionLocal()

    def find_all(self) -> list[CategoryItem]:
        stmt = select(CategoryItem)
        return self.db.scalars(stmt).all()

    def find_by_id(self, item_id: int) -> CategoryItem | None:
        stmt = select(CategoryItem).where(CategoryItem.id == item_id)
        return self.db.scalar(stmt)

    def find_by_name(self, text: str) -> list[CategoryItem]:
        stmt = select(CategoryItem).where(CategoryItem.name.contains(text))
        return self.db.scalars(stmt).all()

    def find_by_category(self, category_id: int) -> list[CategoryItem]:
        stmt = select(CategoryItem).where(CategoryItem.category_id == category_id)
        return self.db.scalars(stmt).all()

    def create_category_item(self, item: CategoryItem) -> CategoryItem:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)

        return item

    def update_category_item(self, item_id: int, **kwargs) -> CategoryItem | None:
        item = self.find_by_id(item_id)

        if item is None:
            return None

        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)

        self.db.commit()
        self.db.refresh(item)

        return item

    def delete_category_item(self, item_id: int) -> bool:
        item = self.find_by_id(item_id)

        if item is None:
            return False

        self.db.delete(item)
        self.db.commit()

        return True
