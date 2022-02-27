import marshmallow

from cornice import Service
from cornice.validators import (
    marshmallow_validator,
)


class UserSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    username = marshmallow.fields.String(required=True)


class UserRequestSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    body = marshmallow.fields.Nested(UserSchema)


users = Service(
    name="users_v1",
    path="/users",
    description="Get and set user data.",
)


@users.post(
    schema=UserRequestSchema,
    validators=(marshmallow_validator,),
    swaggermarsh_show="v1",
    swaggermarsh_request=dict(body=UserSchema),
    swaggermarsh_responses={"201": UserSchema},
)
def get_info(request):
    request.response.status_code = 201
    return {"username": "tester001"}
