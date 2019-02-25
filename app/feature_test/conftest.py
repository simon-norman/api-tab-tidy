from app.app import create_app
from app.extensions import db
import pytest


@pytest.fixture
def test_client():
    app = create_test_app()
    context = app.app_context()
    context.push()

    reset_db()

    yield app.test_client()

    context.pop()


def create_test_app():
    app = create_app()
    app.config['TESTING'] = True
    return app


def reset_db():
    db.drop_all()
    db.create_all()
