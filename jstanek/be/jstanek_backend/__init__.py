import logging

from fastapi import FastAPI
from .root import router_api
from .websockets import router_ws

app = None
logging.basicConfig(level=logging.DEBUG)


def construct_app():
    _app: FastAPI = FastAPI()
    _app.include_router(router_ws)
    _app.include_router(router_api)
    return _app


app = construct_app()
