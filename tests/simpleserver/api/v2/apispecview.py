from pycornmarsh import get_spec


def api_spec(request):
    return get_spec(
        request=request,
        title="PyCornMarsh APISpec API V2.",
        version="2.0.0",
        description="""
        Generates a apispec to api v2 containing endpoints, schemas and can you test the requests
        """,
        security_scheme={
            "JWT": {"type": "apiKey", "in": "header", "name": "Authorization"}
        },
    )
