import hashlib
from typing import Literal


def hash_tool(alg: str, text: str):
    if not text:
        raise ValueError("Missing text")
    if not alg:
        raise ValueError("Missing algorithm")

    _alg = alg.casefold()
    match _alg:
        case "sha-512" | "sha512":
            return hashlib.sha512(bytearray(text, "utf-8")).hexdigest()
        case "sha-256" | "sha256":
            return hashlib.sha256(bytearray(text, "utf-8")).hexdigest()
        case "sha1" | "sha":
            return hashlib.sha1(bytearray(text, "utf-8")).hexdigest()
        case "md5" | "md":
            return hashlib.md5(bytearray(text, "utf-8")).hexdigest()
        case _:
            raise ValueError("Unsupported algorithm")
