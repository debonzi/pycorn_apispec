import pytest
import webtest


from pyramid.paster import get_appsettings

from simpleserver.main import main


@pytest.fixture(scope="session")
def app():
    return main()


@pytest.fixture
def testapp(app):
    testapp = webtest.TestApp(
        app,
        extra_environ={
            "HTTP_HOST": "pycorn.tests.com",
        },
    )

    return testapp
