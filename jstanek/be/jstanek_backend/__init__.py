import logging

from fastapi import FastAPI
from .main import router
from .websockets import routerws

logging.basicConfig(level=logging.INFO)
app: FastAPI = FastAPI()
app.include_router(router)
app.include_router(routerws)
