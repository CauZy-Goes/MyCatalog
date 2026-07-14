from datetime import datetime
from models.entity import Entity
from models.category import Category
from models.category_item import CategoryItem

entity = Entity(
    name="Example Entity",
    address="123 Example St",
    created_at=datetime(2003, 12, 23),
)

print(entity)

category = Category(
    name="Example Category ",
    entity_id=1,
    entity=entity,
)

print(category)

categoryItem = CategoryItem(
    name="Example Category Item",
    category_id=1,
    category=category,
)

print(categoryItem)
