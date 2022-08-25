from typing import Union
from fastapi import FastAPI
from .api import api


app = FastAPI()

app.include_router(api.api_router, prefix="/api", )
def read_root():
    return {"Hello": "World"}
