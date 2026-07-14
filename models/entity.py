"""
Entity
------
Model ORM que representa o estabelecimento dentro do catálogo
(restaurante, barbearia, etc — o "dono" do catálogo).
"""

from datetime import datetime

from typing import List

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database.database import Base


class Entity(Base):
    __tablename__ = "entity"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    phoneNumber: Mapped[int] = mapped_column(Integer, nullable=True)

    categories: Mapped[List["Category"]] = relationship(back_populates="entity")

    def __repr__(self):
        return (
            f"Entity(id={self.id}, name='{self.name}', "
            f"address='{self.address}', created_at={self.created_at})"
        )