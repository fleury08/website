from pyramid.response import Response
from pyramid.view import view_config
import hashlib


@view_config(route_name="hash")
def hash_tool(request):
	r_json = request.json_body
	query = r_json['query']
	alg = r_json['alg']
	resp = ''
	if alg == 'sha-512':
		resp = hashlib.sha512(bytearray(query, 'utf-8')).hexdigest()
	elif alg == 'sha-256':
		resp = hashlib.sha256(bytearray(query, 'utf-8')).hexdigest()
	elif alg == 'sha1':
		resp = hashlib.sha1(bytearray(query, 'utf-8')).hexdigest()
	elif alg == 'md5':
		resp = hashlib.md5(bytearray(query, 'utf-8')).hexdigest()
	return Response(body=resp)
