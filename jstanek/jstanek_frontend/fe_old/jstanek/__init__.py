from pyramid.config import Configurator


def main(global_config, **settings):
	""" This function returns a Pyramid WSGI application.
	"""
	config = Configurator(settings=settings)
	config.include('pyramid_jinja2')
	config.include('.tools')
	config.add_static_view('static', 'static', cache_max_age=3600)
	config.add_route('home', '/')
	config.add_route('password', '/tools/password')
	config.add_route('base64', '/tools/base64')
	config.add_route('hash', '/tools/hash')
	config.add_route('mongo', '/tools/mongo')
	config.scan()
	return config.make_wsgi_app()

