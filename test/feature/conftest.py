from app import create_app
import pytest


@pytest.fixture
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    test_client = app.test_client()

    context = app.app_context()
    context.push()

    yield test_client

    context.pop()