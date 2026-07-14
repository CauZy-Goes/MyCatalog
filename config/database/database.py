"""
database
--------
Configuração central da conexão com o banco de dados: engine,
fábrica de sessões e a Base declarativa usada pelos models ORM.

Usa pymssql (não pyodbc) porque o driver TDS já vem embutido no
próprio pacote pip — não precisa instalar nenhum driver ODBC
separado no Windows.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Ajuste usuário/senha/host/porta conforme o seu docker-compose.yml.
DATABASE_URL = "mssql+pymssql://sa:MyCatalog%40123@localhost:1434/master"

engine = create_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    """Classe base de onde todos os models ORM herdam."""
    pass


def init_db() -> None:
    """
    Cria todas as tabelas mapeadas pelos models ORM, caso ainda não existam.

    Precisa que os models já estejam importados antes de chamar essa
    função, para que fiquem registrados em Base.metadata.
    """
    from models.entity import Entity  # noqa: F401
    from models.category import Category  # noqa: F401
    from models.category_item import CategoryItem  # noqa: F401

    Base.metadata.create_all(engine)