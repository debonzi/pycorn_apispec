from pyramid.config import Configurator


def main():
    with Configurator(
        settings={"dotted_api_module": "tests.simpleserver.api"}
    ) as config:

        config.include("cornice")
        config.include(".api", route_prefix="/api")

    return config.make_wsgi_app()
