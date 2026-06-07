from app.db.base import Base
from app.db.database import engine

from app.models.user import User


def create_tables():
    Base.metadata.create_all(bind=engine)