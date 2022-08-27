from pydantic import BaseModel, HttpUrl, UUID4


class PriceSourceBase(BaseModel):
    name: str
    url: HttpUrl
    persons: int
    selector: str


class PriceSourceInDB(PriceSourceBase):
    id: UUID4

    class Config:
        orm_mode = True


class PriceSource(PriceSourceInDB):
    pass


class PriceSourceCreate(PriceSourceBase):
    pass


class PriceSourceUpdate(PriceSourceBase):
    pass


class PriceSourcesAll(BaseModel):
    value: list[PriceSource]
