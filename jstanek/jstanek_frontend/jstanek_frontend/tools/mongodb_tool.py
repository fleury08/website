from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name="mongo")
def mongodb_tool(request):
	return Response(body=_id_parse(request))


def _id_parse(request):
	from datetime import datetime
	r_json = request.json_body
	query = r_json['query']
	resp = ''
	if query:
		if len(query) == 24:
			timestamp = int(query[:8], 16)
			resp = datetime.fromtimestamp(timestamp)
	return resp.isoformat()
