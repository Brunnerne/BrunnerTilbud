from typing import Union
from fastapi import FastAPI
from .api import api
from .db.init_db import init_db

init_db()

tags_metadata = [
    {
        "name": "priceSource",
        "description": "",
    },
    {"name": "price", "description": ""},
]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(api.api_router, prefix="/api")
