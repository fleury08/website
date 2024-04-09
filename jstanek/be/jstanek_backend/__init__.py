import logging

from fastapi import FastAPI
from .root import router_api
from .websockets import router_ws

logging.basicConfig(level=logging.DEBUG)
app: FastAPI = FastAPI()
app.include_router(router_ws)
app.include_router(router_api)
