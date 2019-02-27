import pytest
import datetime
from app.models.tab import Tab
from app.extensions import db
from flask import Flask


@pytest.fixture(scope="module")
def test_app():
    app = Flask(__name__)
    app.config.from_object('app.config.DevelopmentConfig')
    context = app.app_context()
    context.push()

    return app


@pytest.fixture(scope="module")
def test_tab_db(test_app):
    db.init_app(test_app)
    db.drop_all()
    db.create_all()

    return db


def create_tab_in_db(test_tab_db, tab_id, last_active_timestamp):
    tab = Tab(
        tab_id=tab_id,
        created_timestamp='2019-02-21T14:33:42+00:00',
        closed_timestamp='2019-02-21T15:35:42+00:00',
        last_active_timestamp=last_active_timestamp.isoformat()
    )
    test_tab_db.session.add(tab)
    test_tab_db.session.commit()


@pytest.fixture(scope="module")
def tab_db_with_test_data(test_tab_db):
    last_active_timestamp = datetime.datetime(2019, 2, 21, 14, 35, 0, 0)
  
    for tab_id in range(0, 100):
        create_tab_in_db(test_tab_db, tab_id, last_active_timestamp)

        last_active_timestamp \
            = last_active_timestamp + datetime.timedelta(seconds=60)