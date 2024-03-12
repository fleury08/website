import logging

from fastapi import FastAPI
from .main import router

logging.basicConfig(level=logging.INFO)
app: FastAPI = FastAPI()
app.include_router(router)
