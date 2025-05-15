from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('pyramid_tm')
        config.include('.models')
        config.include('.routes')
        config.add_static_view(name='static', path='static', cache_max_age=3600)
        config.add_route('home', '/')
        config.add_route('mahasiswa', '/mahasiswa')
        config.add_route('api_mahasiswa', '/api/mahasiswa')
        config.add_route('api_mahasiswa_detail', '/api/mahasiswa/{id}')
        config.scan()
    return config.make_wsgi_app()
