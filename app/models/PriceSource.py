from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy.orm import relationship
from .Price import Price
from uuid import uuid4
from app.db.base import Base


class PriceSource(Base):
    __tablename__ = "price_source"

    id = Column(CHAR(32), primary_key=True, index=True, default=lambda: uuid4().hex)
    name = Column(String)
    url = Column(String)
    persons = Column(Integer)
    selector = Column(String)

    prices = relationship("Price", back_populates="priceSource")

    def __repr__(self):
        return f"PriceSource(id='{self.id}', name='{self.name}')"
