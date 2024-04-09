import hashlib
import logging
from dataclasses import dataclass
from functools import cache
from typing import Literal

type SupportedAlgorithms = Literal[
    "sha-512", "sha512", "sha-256", "sha256", "sha1", "sha", "md5", "md"
]


@dataclass(slots=True)
class HashContainer:
    text: str = ""
    alg: SupportedAlgorithms = "sha-512"


def hash_text(to_hash: HashContainer):
    if not to_hash:
        raise ValueError("Missing hash container, cannot hash")
    if not to_hash.text:
        raise ValueError("Missing text, cannot hash")
    if not to_hash.alg:
        logging.info("Missing algorithm, using default")
        to_hash.alg = "sha-512"

    match to_hash.alg.casefold():
        case "sha-512" | "sha512":
            return hashlib.sha512(bytearray(to_hash.text, "utf-8")).hexdigest()
        case "sha-256" | "sha256":
            return hashlib.sha256(bytearray(to_hash.text, "utf-8")).hexdigest()
        case "sha1" | "sha":
            return hashlib.sha1(bytearray(to_hash.text, "utf-8")).hexdigest()
        case "md5" | "md":
            return hashlib.md5(bytearray(to_hash.text, "utf-8")).hexdigest()
        case _:
            raise ValueError("Unsupported algorithm")
