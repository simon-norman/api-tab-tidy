import pytest
import datetime
from flask import Flask
from app.extensions import db
from app.models.tab import Tab
from app.app import create_app
from app.models.inactive_tab_rec import InactiveTabRecording


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def test_client(test_app):
    context = test_app.app_context()
    context.push()

    db.drop_all()
    db.create_all()

    yield test_app.test_client()

    context.pop()


@pytest.fixture(scope="module")
def test_flask_shell():
    app = Flask(__name__)
    app.config.from_object('app.config.DevelopmentConfig')
    context = app.app_context()
    context.push()

    yield app

    context.pop()


@pytest.fixture()
def test_tab_db(test_flask_shell):
    db.init_app(test_flask_shell)
    db.session.commit()
    db.drop_all()
    db.create_all()

    return db


@pytest.fixture(scope="module")
def new_tab():
    return {
        'tabId': 1,
        'createdTimestamp': '2019-02-21T14:33:42+00:00',
    }


@pytest.fixture
def saved_tab(new_tab, test_tab_db):
    tab = create_tab_in_db(
        test_tab_db=test_tab_db,
        tab_id=new_tab['tabId'],
        created_timestamp=new_tab['createdTimestamp']
    )
    return tab


def create_tab_in_db(test_tab_db, tab_id, created_timestamp):
    tab = Tab(
        tab_id=tab_id,
        created_timestamp=created_timestamp,
    )
    test_tab_db.session.add(tab)
    test_tab_db.session.commit()
    return tab


def create_inactive_tab_rec_in_db(
    test_tab_db,
    tab_id,
    last_active_timestamp
):
    active_timestamp = last_active_timestamp - datetime.timedelta(seconds=60)
    inactive_tab_rec = InactiveTabRecording(
        tab_id=tab_id,
        active_timestamp=active_timestamp.isoformat(),
        inactive_timestamp=last_active_timestamp,
    )

    test_tab_db.session.add(inactive_tab_rec)
    test_tab_db.session.commit()


@pytest.fixture()
def saved_inactive_tab_recs(test_tab_db):
    last_active_timestamp = datetime.datetime(2020, 1, 1, 0, 5)
    created_timestamp = datetime.datetime(2020, 1, 1)
    inactive_tab_recs = []

    for tab_id in range(0, 100):
        create_tab_in_db(test_tab_db, tab_id, created_timestamp)
        inactive_tab_recs.append(create_inactive_tab_rec_in_db(
            test_tab_db,
            tab_id,
            last_active_timestamp
        ))

        last_active_timestamp \
            = last_active_timestamp + datetime.timedelta(seconds=60)

    return inactive_tab_recs
