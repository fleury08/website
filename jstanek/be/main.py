import json
from builtins import BaseException

from tools import base64_tool, hash_tool, mongodb_tool, passsword_generator
from fastapi import FastAPI
from dataclasses import dataclass, Field
import string
import random

app = FastAPI()


@dataclass
class Result:
    result: str | None = None
    error: bool = False
    error_text: str | None = None

    def __str__(self):
        return json.dumps(self.__dict__)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/password")
async def create_password(
    length: int = 16,
    lowercase: bool = True,
    uppercase: bool = True,
    numbers: bool = True,
    symbols: bool = True,
):
    if not length:
        return Result(result="", error=True, error_text="Empty length")
    if lowercase or uppercase or numbers or symbols:
        return Result(
            result=passsword_generator.generate_password(
                uppercase=uppercase,
                lowercase=lowercase,
                numbers=numbers,
                symbols=symbols,
                length=length,
            )
        )
    return Result(result="", error=True, error_text="Empty options")


@app.get("/base64/encode/{to_encode}")
async def base64_encode(to_encode: str):
    if not to_encode:
        return Result(result="", error=True, error_text="Empty string")
    try:
        return Result(result=str(base64_tool.base64_encode(to_encode)))
    except BaseException as be:
        return Result(result=str(be), error=True, error_text="Invalid base64 string")


@app.get("/base64/decode/{to_decode}")
async def base64_decode(to_decode: bytes):
    if not to_decode:
        return Result(result="", error=True, error_text="Empty string")
    try:
        return Result(result=str(base64_tool.base64_decode(to_decode)))
    except BaseException as be:
        return Result(result=str(be), error=True, error_text="Invalid base64 string")


@app.get("/hash/{alg}/{value}")
async def hash(alg: str, value: str):
    if not alg or not value:
        return Result(result="", error=True, error_text="Empty string")
    try:
        return Result(result=str(hash_tool.hash_tool(alg, value)))
    except ValueError as ve:
        return Result(result=str(ve), error=True, error_text="Hashing error")


@app.get("/mongo/{mongo_id}")
async def parse_mongo_id(mongo_id: str):
    if not mongo_id:
        return Result(result="", error=True, error_text="Empty string")
    try:
        return Result(result=str(mongodb_tool.mongo_id_parse(mongo_id)))
    except BaseException as be:
        return Result(result=str(be), error=True, error_text="Invalid mongo id")
