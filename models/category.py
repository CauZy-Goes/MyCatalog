from datetime import datetime

from typing import List

from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database.database import Base


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    entity_id: Mapped[int] = mapped_column(ForeignKey("entity.id"), nullable=False)
    order: Mapped[int] = mapped_column(Integer, nullable=False)

    entity: Mapped["Entity"] = relationship(back_populates="categories")
    items: Mapped[List["CategoryItem"]] = relationship(back_populates="category")

    def __repr__(self):
        return (
            f"Category(id={self.id}, name='{self.name}', entity_id={self.entity_id}), Entity={self.entity}), Order={self.order}"
        )