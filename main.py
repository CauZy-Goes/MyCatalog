from datetime import datetime
from models.entity import Entity
from models.category import Category

entity = Entity(
    name="Example Entity",
    address="123 Example St",
    created_at=datetime(2003, 12, 23),
)

print(entity)

category = Category(
    name="Example Category ",
    entity_id=1,
)

print(category)
