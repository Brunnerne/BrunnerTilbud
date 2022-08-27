from typing import Generator
from app.db.session import SessionLocal
from sqlalchemy.orm import Session


def get_db() -> Generator:
    db = SessionLocal()
    db.current_user_id = None
    try:
        yield db
    finally:
        db.close()
