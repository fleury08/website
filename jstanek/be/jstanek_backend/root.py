import logging
from http import HTTPStatus

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from .tools import base64_tool, hash_tool, mongodb_tool, passsword_generator
from .tools.base64_tool import Base64Object
from .tools.hash_tool import HashObject
from .tools.mongodb_tool import MongoDbObject
from .tools.passsword_generator import PasswordOptions

router_api = APIRouter(
    dependencies=[],
    prefix="/api",
    tags=["root"],
    responses={404: {"description": "Not found"}},
)


@router_api.get("/")
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
async def hash_value(to_hash: HashObject):
    logging.info(to_hash)
    try:
        return {"result": hash_tool.hash_text(to_hash)}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))


@router_api.post("/convert/mongodb/id")
async def parse_mongo_id(mdb_obj: MongoDbObject):
    logging.info(mdb_obj)
    try:
        return {"result": str(mongodb_tool.mongo_id_parse(mdb_obj))}
    except ValueError as ve:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=str(ve))
