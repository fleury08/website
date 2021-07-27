import unittest
from ..base64_tool import *
from pyramid.testing import DummyRequest


class Base64ToolTest(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.s = 'test'

	def test_base64_decode(self):
		r = DummyRequest(path=f'/api/v1/base64/decode/{base64_encode(self.s).hex()}', method='GET')
		resp = str(base64_tool(r).body, encoding='utf-8')
		self.assertEqual(resp, self.s)

	def test_base64_encode(self):
		r = DummyRequest(path=f'/api/v1/base64/encode/{self.s}', method='GET')
		self.assertEqual(base64_tool(r).body, b'dGVzdA==')
