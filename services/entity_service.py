from sqlalchemy.orm import Session
from sqlalchemy import select

from models.entity import Entity

from datetime import datetime

from config.database.database import SessionLocal


class EntityService:

    # def __init__(self, db: Session):
    #     self.db = db

    def __init__(self):
        self.db = SessionLocal()

    def find_all(self) -> list[Entity]:
        #return self.db.query(Entity).all()
        stmt = select(Entity)
        entities = list(self.db.scalars(stmt).all())
        return entities

    def find_by_id(self, entity_id: int) -> Entity | None:
        
        # return (
        #     self.db.query(Entity)
        #     .filter(Entity.id == entity_id)
        #     .first()
        # )
        
        ##return self.db.get(Entity, entity_id)
        stmt = select(Entity).where(Entity.id == entity_id)
        entity = self.db.scalar(stmt)
        return entity
    
    def find_by_name(self, text: str) -> list[Entity]:
        stmt = select(Entity).where(Entity.name.contains(text))
        return list(self.db.scalars(stmt).all())
        # return (
        # self.db.query(Entity)
        # .filter(Entity.name.like(f"%{name}%"))
        # .all()
        #     )

    def create_entity(self, entity: Entity) -> Entity:

        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def update_entity(self, entity_id: int, **kwargs) -> Entity | None:
        entity = self.find_by_id(entity_id)

        if entity is None:
            return None

        for key, value in kwargs.items():
            if hasattr(entity, key):
                setattr(entity, key, value)

        self.db.commit()
        self.db.refresh(entity)

        return entity

    def delete_entity(self, entity_id: int) -> bool:
        entity = self.find_by_id(entity_id)

        if entity is None:
            return False

        self.db.delete(entity)
        self.db.commit()

        return True