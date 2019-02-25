from app.app import create_app
from app.extensions import db
import pytest


@pytest.fixture
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    test_client = app.test_client()

    context = app.app_context()
    context.push()

    reset_db()

    yield test_client

    context.pop()


def reset_db():
    db.drop_all()
    db.create_all()
