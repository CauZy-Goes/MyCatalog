from datetime import datetime
from models.entity import Entity

entity = Entity(
    name="Example Entity",
    address="123 Example St",
    created_at=datetime(2003, 12, 23),
)

print(entity)