def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('password', '/tools/password')
    config.add_route('base64', '/tools/base64')
    config.add_route('hash', '/tools/hash')
    config.add_route('mongo', '/tools/mongo')
