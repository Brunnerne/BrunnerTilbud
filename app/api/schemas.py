from pydantic import BaseModel

class PriceSource(BaseModel):
    name: str
    url: str
    persons: int
    selector: str

class PriceSources(BaseModel):
    values: list[PriceSource]
