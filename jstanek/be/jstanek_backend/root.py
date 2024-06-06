import logging
from http import HTTPStatus

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from .tools import (
    base64_tool,
    hash_tool,
    mongodb_tool,
    passsword_generator,
    qrcode_tool,
)
from .tools.base64_tool import Base64Object
from .tools.hash_tool import HashContainer
from .tools.mongodb_tool import MongoDbContainer
from .tools.passsword_generator import PasswordOptions
from .tools.qrcode_tool import QrCodeContainer


router_api = APIRouter(
    dependencies=[],
    prefix="/api",
    tags=["root"],
    responses={404: {"description": "Not found"}},
)


@router_api.get("")
async def read_root():
    return {"Hello": "World"}


@router_api.post("/password")
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


@router_api.post("/base64/encode")
async def base64_encode(b64object: Base64Object):
    logging.info(b64object)
    try:
        return {"result": str(base64_tool.base64_encode(b64object), "utf-8")}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))


@router_api.post("/base64/decode")
async def base64_decode(b64object: Base64Object):
    logging.info(b64object)
    try:
        return {"result": str(base64_tool.base64_decode(b64object), "utf-8")}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))


@router_api.post("/hash")
async def hash_value(to_hash: HashContainer):
    logging.info(to_hash)
    try:
        return {"result": hash_tool.hash_text(to_hash)}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))


@router_api.post("/convert/mongodb/id")
async def parse_mongo_id(mdb_obj: MongoDbContainer):
    logging.info(mdb_obj)
    try:
        return {"result": str(mongodb_tool.mongo_id_parse(mdb_obj))}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))


@router_api.post("/qrcode")
async def qr_code(qr_obj: QrCodeContainer):
    logging.info(qr_obj)
    try:
        if not qr_obj.text:
            raise ValueError("Missing text, cannot generate qrcode")
        if len(qr_obj.text) > 2048:
            raise ValueError("Text too long, cannot generate qrcode")
        return {"result": str(qrcode_tool.generate_qrcode(qr_obj).decode("utf-8"))}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))
