import pytest

import kubelinks_app.config as config
from kubelinks_app import create_app


@pytest.fixture()
def app():
    app = create_app(config.Config)

    # other setup can go here

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
