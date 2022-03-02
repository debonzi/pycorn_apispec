import marshmallow

from cornice import Service
from cornice.validators import (
    marshmallow_validator,
    marshmallow_body_validator,
    marshmallow_headers_validator,
    marshmallow_querystring_validator,
)


class UserSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    username = marshmallow.fields.String(required=False)


class UserHTTPSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    body = marshmallow.fields.Nested(UserSchema)


users = Service(
    name="users_v2",
    path="/users",
    description="Get and set user data.",
)


@users.get(
    schema=UserSchema,
    validators=(marshmallow_querystring_validator,),
    pcm_show="v2",
    pcm_request=dict(body=UserSchema),
    pcm_responses={200: UserSchema}
)
def get_info(request):
    return [{"username": "tester002"}]
