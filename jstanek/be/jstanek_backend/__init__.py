import logging

from fastapi import FastAPI
from .root import router_api
from .websockets import router_ws

app = None


def construct_app():
    logging.basicConfig(level=logging.DEBUG)
    _app: FastAPI = FastAPI()
    _app.include_router(router_ws)
    _app.include_router(router_api)
    return _app


if __name__ == "__main__":
    app = construct_app()
