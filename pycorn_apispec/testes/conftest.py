import pytest
from apispec import APISpec
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.testing import DummyRequest, testConfig
from webtest import TestApp as WebTestApp  # Avoid pytest warning

from pyramid_apispec import __version__
from pyramid_apispec.helpers import add_pyramid_paths


@pytest.fixture
def config():
    """Pyramid test `Configurator` harness."""
    with testConfig(request=DummyRequest()) as config:
        yield
