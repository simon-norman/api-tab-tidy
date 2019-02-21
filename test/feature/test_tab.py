import pytest
from app import create_app


@pytest.fixture
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    test_client = app.test_client()

    context = app.app_context()
    context.push()

    yield test_client

    context.pop()


def test_smoke_api(test_client):
    response = test_client.get('/graphql')
