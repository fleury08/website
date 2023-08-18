import json

import base64


def base64_encode(to_encode: str) -> bytes:
    if not to_encode:
        return b""
    return base64.b64encode(to_encode.encode("utf-8"))


def base64_decode(to_decode: bytes) -> bytes:
    if not to_decode:
        return b""
    try:
        return base64.b64decode(to_decode)
    except Exception:
        return b""
