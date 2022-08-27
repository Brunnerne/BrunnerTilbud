from uuid import uuid4
from sqlalchemy import Column, String, Integer, CHAR, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now
from app.db.base import Base


class Price(Base):
    __tablename__ = "price"

    id = Column(CHAR(32), primary_key=True, default=lambda: uuid4().hex)
    price = Column(Integer)
    checkedAt = Column(DateTime, default=now())

    priceSourceId = Column(String, ForeignKey("price_source.id"))
    priceSource = relationship("PriceSource", back_populates="prices")

    def __repr__(self):
        return f"PriceSource(id='{self.id}', price='{self.price}')"
