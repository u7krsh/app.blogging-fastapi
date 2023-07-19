from typing import Generator

from backend.core.config import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL_STRING = Settings.DATABASE_URL
print(f"DataBase URL is {DB_URL_STRING}")

engine = create_engine(DB_URL_STRING)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()
