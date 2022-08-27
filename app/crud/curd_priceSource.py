from .base import CRUDBase
from app.models.PriceSource import PriceSource
from app.schemas import PriceSourceCreate, PriceSourceUpdate


class CRUDPriceSource(CRUDBase[PriceSource, PriceSourceCreate, PriceSourceUpdate]):
    pass


priceSource = CRUDPriceSource(PriceSource)
