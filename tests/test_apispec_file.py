def test_openapi_v1(testapp):
    resp = testapp.get("/api/v1/openapi.json")
    assert resp.json == {
        "paths": {
            "/api/v1/users": {
                "post": {
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/UserSchema"}
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/UserSchema"
                                    }
                                }
                            },
                        }
                    },
                }
            }
        },
        "info": {
            "title": "PyCornMarsh APISpec API V1.",
            "version": "1.0.0",
            "description": "\n        Generates a apispec to api v1 containing endpoints, schemas and can you test the requests\n        ",
        },
        "openapi": "3.0.2",
        "components": {
            "schemas": {
                "UserSchema": {
                    "type": "object",
                    "properties": {"username": {"type": "string"}},
                    "required": ["username"],
                }
            },
            "securitySchemes": {
                "JWT": {"type": "apiKey", "in": "header", "name": "Authorization"}
            },
        },
        "servers": [{"url": "http://pycorn.tests.com"}],
    }


def test_openapi_v2(testapp):
    resp = testapp.get("/api/v2/openapi.json")
    assert resp.json == {
        "paths": {
            "/api/v2/users": {
                "get": {
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/UserSchema"}
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/UserSchema"
                                    }
                                }
                            },
                        }
                    },
                }
            }
        },
        "info": {
            "title": "PyCornMarsh APISpec API V2.",
            "version": "2.0.0",
            "description": "\n        Generates a apispec to api v2 containing endpoints, schemas and can you test the requests\n        ",
        },
        "openapi": "3.0.2",
        "components": {
            "schemas": {
                "UserSchema": {
                    "type": "object",
                    "properties": {"username": {"type": "string"}},
                }
            },
            "securitySchemes": {
                "JWT": {"type": "apiKey", "in": "header", "name": "Authorization"}
            },
        },
        "servers": [{"url": "http://pycorn.tests.com"}],
    }
