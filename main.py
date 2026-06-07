from fastapi import FastAPI

from app.core.config import settings
from app.api.health import router as health_router
from app.db.init_db import create_tables

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    create_tables()


app.include_router(health_router)


@app.get("/")
def root():
    return {
        "service": settings.APP_NAME,
        "status": "running"
    }