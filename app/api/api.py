from fastapi import APIRouter, Depends, HTTPException
from .deps import get_db
from app import crud
from app.schemas import PriceSourceCreate, PriceSource
from sqlalchemy.orm import Session

from app import schemas

api_router = APIRouter()


@api_router.get(
    "/priceSources", response_model=schemas.PriceSourcesAll, tags=["priceSource"]
)
def get_all_prices_source(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100
):
    """
    Get all price sources
    """
    sources = crud.priceSource.get_multi(db=db, skip=skip, limit=limit)
    result = {"value": sources}
    return result


@api_router.get(
    "/priceSources/{priceSourceId}",
    response_model=schemas.PriceSource,
    tags=["priceSource"],
)
def get_price_source(priceSourceId: str, db: Session = Depends(get_db)):
    """
    Get a price source by id

    """
    source = crud.priceSource.get(db, priceSourceId)

    if not source:
        raise HTTPException(
            status_code=404, detail=f"PriceSource with id '{id}' not found"
        )


@api_router.post("/priceSources", tags=["priceSource"], response_model=PriceSource)
def create_price_soruce(
    price_source: PriceSourceCreate,
    db: Session = Depends(get_db),
):
    return crud.priceSource.create(db, obj_in=price_source)


@api_router.delete("/priceSources/{priceSourceId}", tags=["priceSource"])
def delete_price_source(priceSourceId: str, db: Session = Depends(get_db)) -> None:
    crud.priceSource.remove(db, priceSourceId)
    return


@api_router.get("/prices", response_model=schemas.PriceAll, tags=["price"])
def prices(db=Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Get all prices
    """
    prices = crud.price.get_multi(db, skip=skip, limit=limit)
    return {"value": prices}


@api_router.get(
    "/priceSources/{priceSourceId}/prices",
    response_model=schemas.PriceAll,
    tags=["price"],
)
def pricesByPriceSource(priceSourceId: str, db: Session = Depends(get_db)):
    """
    Get prices from a price source
    """
    prices = crud.price.get_by_priceSource(db, priceSourceId)
    return {"value": prices}
