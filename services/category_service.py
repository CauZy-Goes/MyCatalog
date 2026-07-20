from sqlalchemy import func, select, update

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
    
    def _normalize_order(
        self,
        entity_id: int,
        desired_order: int
    ) -> int:
        """
        Ajusta o order informado para uma posição válida.

        Regras:

        - Se for menor que 1, vira 1.
        - Se for maior que o último + 1,
        vira último + 1.

        Exemplos:

            Orders atuais:
                1
                2
                3

            desired_order = -5

            Resultado:
                1

        ----------------------------

            Orders atuais:
                1
                2
                3

            desired_order = 100

            Resultado:
                4
        """

        last_order = self._get_last_order(entity_id)

        if desired_order < 1:
            return 1

        if desired_order > last_order + 1:
            return last_order + 1

        return desired_order
    
    def _shift_orders_up(
        self,
        entity_id: int,
        starting_order: int
    ):
        """
        Desloca todas as categorias para cima (+1),
        abrindo espaço para uma nova categoria.

        Exemplo:

            Antes

                1
                2
                3
                4

            Inserindo na posição 2

            Depois

                1
                3
                4
                5

        A nova categoria poderá ser inserida na posição 2.
        """

        stmt = (
            update(Category)
            .where(
                Category.entity_id == entity_id,
                Category.order >= starting_order
            )
            .values(order=Category.order + 1)
        )

        self.db.execute(stmt)

    def _close_gap(
        self,
        entity_id: int,
        deleted_order: int
    ):
        """
        Fecha o espaço deixado por uma categoria removida.

        Exemplo:

            Antes

                1
                2
                3
                4

            Remove order 2

            Depois

                1
                2
                3
        """

        stmt = (
            update(Category)
            .where(
                Category.entity_id == entity_id,
                Category.order > deleted_order
            )
            .values(order=Category.order - 1)
        )

        self.db.execute(stmt)
    
    
