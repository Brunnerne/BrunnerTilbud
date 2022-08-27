from app.models.Price import Price
from app.schemas import PriceCreate, PriceUpdate
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Any, Optional
from .base import CRUDBase


class CRUDPrice(CRUDBase[Price, PriceCreate, PriceUpdate]):
    def get_by_priceSource(self, db: Session, id: str) -> Optional[list[Price]]:
        stmt = select(Price).where(Price.priceSourceId == id)
        return db.execute(stmt).scalars().all()


price = CRUDPrice(Price)
