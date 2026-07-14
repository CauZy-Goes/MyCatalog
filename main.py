from datetime import datetime
from models.entity import Entity
from models.category import Category
from models.category_item import CategoryItem

from services.entity_service import EntityService

from config.database.database import init_db

if __name__ == "__main__":
    init_db() 

entityService = EntityService()

# print("All entities:")
# entities = entityService.find_all()
# for entity in entities:
#     print(entity)

print(entityService.find_by_name("Co"))

entity = Entity(
    name="Coco Bambu",
    address="Shooping Paralela",
    created_at=datetime(1999, 2, 13),
    phoneNumber=987654321,
    email="coco@gmail.com",
    description="Restaurante de frutos do mar"
)

# entityService = EntityService()

# entityService.create_entity(
#     Entity(
#         name="Construação Aqui",
#         address="Lauro De freitas",
#         created_at=datetime(2023, 12, 23),
#         phoneNumber=123456789,
#         email="contruaaqui@gmail.com",
#         description="Empresa de construção civil"
#     )
# )

# entityService.create_entity(entity)

# print(entityService.delete_entity(10))


# targetEntity = entityService.find_by_id(9)
# targetEntity.name = "Coco Caju"

# print(targetEntity)

# print(entityService.update_entity(targetEntity.id, name=targetEntity.name))

# print(targetEntity)


#print(entity)

# category = Category(
#     name="Example Category ",
#     entity_id=1,
#     entity=entity,
# )

# print(category)

# categoryItem = CategoryItem(
#     name="Example Category Item",
#     category_id=1,
#     category=category,
# )

# print(categoryItem)
