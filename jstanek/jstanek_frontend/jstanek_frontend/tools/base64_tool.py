from pyramid.response import Response
from pyramid.request import Request
from pyramid.view import view_config
import base64


@view_config(route_name="base64")
def base64_tool(request: Request):
	r_json = request.json_body
	query = r_json['query']
	method = r_json['method']
	if method:
		if method == 'encode':
			return Response(body=base64_encode(query), status=200)
		if method == 'decode':
			return Response(body=base64_decode(query), status=200)
	return Response(body="", status=500)


def base64_encode(to_encode: str):
	if not to_encode:
		return ''
	return base64.b64encode(bytearray(str(to_encode), encoding='utf-8'))


def base64_decode(to_decode: bytes):
	if not to_decode:
		return ''
	try:
		return base64.b64decode(to_decode)
	except Exception:
		return ""
