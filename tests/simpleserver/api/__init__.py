def includeme(config):
    config.include("pycorn_apispec")

    config.include(".v1", route_prefix="/v1")
    config.include(".v2", route_prefix="/v2")
