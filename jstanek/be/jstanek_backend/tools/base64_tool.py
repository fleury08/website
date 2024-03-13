import base64
from dataclasses import dataclass


@dataclass
class Base64Object:
    text: str


def base64_encode(to_encode: Base64Object) -> bytes:
    if not to_encode or not to_encode.text:
        raise ValueError("Empty string to encode, cannot encode")
    return base64.b64encode(to_encode.text.encode("utf-8"))


def base64_decode(to_decode: Base64Object) -> bytes:
    if not to_decode or not to_decode.text:
        return b""
    try:
        return base64.b64decode(to_decode.text)
    except Exception:
        return b""
