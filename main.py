from fastapi import FastAPI

from config.database.database import init_db

from controllers.entity_controller import router as entity_router
from controllers.category_controller import router as category_router

app = FastAPI(
    title="My Catalog API",
    version="1.0.0"
)

init_db()

app.include_router(entity_router)
app.include_router(category_router)

# uvicorn main:app --reload