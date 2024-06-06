import unittest

from . import qrcode_tool


class TestQrCodeTool(unittest.TestCase):
    def test_qrgenerator(self):
        obj = qrcode_tool.QrCodeContainer(text="test")
        render = ",".join(
            [
                "data:image/png;base64",
                qrcode_tool.generate_qrcode(obj).decode("utf-8"),
            ]
        )
