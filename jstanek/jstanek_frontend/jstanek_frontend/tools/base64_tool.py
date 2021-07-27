import json

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.response import Response
from pyramid.request import Request
from pyramid.view import view_config
import base64


@view_config(route_name="base64", request_method='POST', renderer='json')
def base64_tool(request: Request):
	r_json = request.json_body
	query = r_json['query']
	method = r_json['method']
	if method:
		if method == 'encode':
			return {'result': str(base64_encode(query), encoding='utf-8')}
		if method == 'decode':
			return {'result': str(base64_decode(query), encoding='utf-8')}
	return HTTPBadRequest()


def base64_encode(to_encode: str) -> bytes:
	if not to_encode:
		return b''
	return base64.b64encode(to_encode.encode('utf-8'))


def base64_decode(to_decode: bytes) -> bytes:
	if not to_decode:
		return b''
	try:
		return base64.b64decode(to_decode)
	except Exception:
		return b''
