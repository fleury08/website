import base64
import io

import qrcode
from dataclasses import dataclass


@dataclass(slots=True)
class QrCodeContainer:
    text: str


def generate_qrcode(to_encode: QrCodeContainer) -> bytes:
    with io.BytesIO() as image_bytes:
        qrcode.make(to_encode.text).save(image_bytes)
        image_bytes.seek(0)
        return base64.b64encode(image_bytes.read())
