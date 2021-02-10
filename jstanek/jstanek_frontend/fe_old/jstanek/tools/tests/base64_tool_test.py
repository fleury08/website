import unittest
from ..base64_tool import *
from pyramid.testing import DummyRequest


class Base64ToolTest(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.s = 'test'

	def test_base64_decode(self):
		r = DummyRequest(json_body={
			'query': base64_encode(self.s),
			'method': 'decode'
		}, method='POST')
		resp = str(base64_tool(r).body, encoding='utf-8')
		self.assertEqual(resp, self.s)

	def test_base64_encode(self):
		r = DummyRequest(json_body={
			'query': self.s,
			'method': 'encode'
		}, method='POST')
		self.assertEqual(base64_tool(r).body, b'dGVzdA==')
