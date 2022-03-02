from pyramid.config import Configurator


def main():
    with Configurator() as config:

        config.include("cornice")
        config.include(".views.api", route_prefix="/api")

    return config.make_wsgi_app()
