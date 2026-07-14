from datetime import datetime

from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database.database import Base


class CategoryItem(Base):
    __tablename__ = "category_item"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    price: Mapped[int] = mapped_column(Integer, nullable=True)
    order: Mapped[int] = mapped_column(Integer, nullable=False)

    category: Mapped["Category"] = relationship(back_populates="items")

    def __repr__(self):
        return (
            f"CategoryItem(id={self.id}, name='{self.name}', category_id={self.category_id}), Category={self.category}), Price={self.price}, Description='{self.description}'"
            f", Order={self.order}"
        )