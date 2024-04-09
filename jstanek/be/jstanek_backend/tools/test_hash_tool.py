import unittest
from . import hash_tool


class TestHashTool(unittest.TestCase):
    def setUp(self):
        self.test_text = "test"
        self.test_hash_sha512 = "ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff"
        self.test_hash_sha256 = (
            "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
        )
        self.test_hash_sha1 = "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"

    def test_hash_text(self):
        obj = hash_tool.HashObject(text=self.test_text, alg="sha-512")
        self.assertEqual(
            hash_tool.hash_text(obj),
            self.test_hash_sha512,
        )

        obj.alg = "sha-256"
        self.assertEqual(
            hash_tool.hash_text(obj),
            self.test_hash_sha256,
        )

        obj.alg = "sha1"
        self.assertEqual(
            hash_tool.hash_text(obj),
            self.test_hash_sha1,
        )
