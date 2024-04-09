import logging

from fastapi import FastAPI
from .main import router
from .websockets import routerws

app = None


def construct_app():
    logging.basicConfig(level=logging.INFO)
    _app: FastAPI = FastAPI()
    _app.include_router(router)
    _app.include_router(routerws)
    return _app


if __name__ == "__main__":
    app = construct_app()
