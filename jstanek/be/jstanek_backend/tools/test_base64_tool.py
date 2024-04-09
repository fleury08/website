import unittest

from . import base64_tool


class TestBase64Tool(unittest.TestCase):
    def setUp(self):
        self.test_object = base64_tool.Base64Object(text="test")
        self.test_object_bytes = self.test_object.text.encode("utf-8")
        self.test_encoded = base64_tool.Base64Object(text="dGVzdA==")
        self.test_encoded_bytes = self.test_encoded.text.encode("utf-8")

    def test_base64_encode(self):
        self.assertEqual(
            base64_tool.base64_encode(self.test_object), self.test_encoded_bytes
        )

    def test_base64_decode(self):
        self.assertEqual(
            base64_tool.base64_decode(self.test_encoded), self.test_object_bytes
        )
