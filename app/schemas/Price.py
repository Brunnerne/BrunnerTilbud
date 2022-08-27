from datetime import datetime
from pydantic import BaseModel


class PriceBase(BaseModel):
    price: int
    priceSourceId: str
    checkedAt: datetime


class PriceInDB(PriceBase):
    id: str

    class Config:
        orm_mode = True


class Price(PriceInDB):
    pass


class PriceUpdate(PriceBase):
    pass


class PriceCreate(PriceInDB):
    pass


class PriceAll(BaseModel):
    value: list[Price]
