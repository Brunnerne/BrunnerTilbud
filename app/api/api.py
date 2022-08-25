from fastapi import APIRouter

from . import schemas

api_router = APIRouter()


@api_router.get("/priceSources", response_model=schemas.PriceSources)
def priceSources():
    return {
            "values": [
                {
                    "name": "konditor-bager",
                    "url": "https://www.konditor-bager.dk/fjerritslev/kagemaendkoner/1032-430-kagemand-kone-brunsviger.html#/42-kagetype-kagemand/44-storrelse-12_14_personer/47-topping_slik-nej_tak/87-topping_marcipan-nej_tak/134-topping_chokolade-nej_tak",
                    "persons": 13,
                    "selector": "#main-product-wrapper > div > div.col-md-8.col-product-info > div.product_header_container.clearfix > div > div:nth-child(1) > div > span > span"
                    },
                {
                    "name": "konditor-bager",
                    "url": "https://www.konditor-bager.dk/fjerritslev/kagemaendkoner/1032-432-kagemand-kone-brunsviger.html#/42-kagetype-kagemand/46-storrelse-20_24_personer_40_kr/47-topping_slik-nej_tak/87-topping_marcipan-nej_tak/134-topping_chokolade-nej_tak",
                    "persons": 22,
                    "selector": "#main-product-wrapper > div > div.col-md-8.col-product-info > div.product_header_container.clearfix > div > div:nth-child(1) > div > span > span"
                    },
                {
                    "name": "føtex",
                    "url": "https://www.foetexudafhuset.dk/product/kagemand-af-brunsviger/",
                    "persons": 25,
                    "selector": "#no-scroll-background > div > div > div > div > div > div > div > div.flex.d-flex.xs12.sm12.md4.lg4 > div > div > div > div.mb-32 > div.price"
                    },
                {
                    "name": "bilka",
                    "url": "https://www.bilkamadudafhuset.dk/product/kagemand/",
                    "persons": 20,
                    "selector": "#no-scroll-background > div.no-product-count > div > div > div > div > div > div > div.flex.d-flex.xs12.sm12.md4.lg4 > div > div > div > div.mb-3 > div.price"
                    },
                ]
            }
