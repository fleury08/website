import logging
from http import HTTPStatus

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from .tools import base64_tool, hash_tool, mongodb_tool, passsword_generator
from .tools.hash_tool import HashObject
from .tools.passsword_generator import PasswordOptions

router = APIRouter(prefix="")


@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.post("/password")
async def create_password(
    password_options: PasswordOptions = None,
):
    logging.info(password_options)
    if password_options:
        try:
            generated_pass = passsword_generator.generate_password(password_options)
            return {"result": generated_pass}
        except ValueError as ve:
            raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))

    raise HTTPException(HTTPStatus.BAD_REQUEST, detail="Invalid password options")


@router.get("/base64/encode/{to_encode}")
async def base64_encode(to_encode: str):
    logging.info(to_encode)
    try:
        return {"result": str(base64_tool.base64_encode(to_encode))}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))


@router.get("/base64/decode/{to_decode}")
async def base64_decode(to_decode: bytes):
    logging.info(to_decode)
    try:
        return {"result": str(base64_tool.base64_decode(to_decode))}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))


@router.post("/hash")
async def hash_value(to_hash: HashObject):
    logging.info(to_hash)
    try:
        return {"result": hash_tool.hash_text(to_hash)}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))


@router.get("/mongo/{mongo_id}")
async def parse_mongo_id(mongo_id: str):
    logging.info(mongo_id)
    try:
        return {"result": str(mongodb_tool.mongo_id_parse(_id=mongo_id))}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))


