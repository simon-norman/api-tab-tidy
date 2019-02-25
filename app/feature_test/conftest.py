from app.app import create_app
from app.extensions import db
from app.models.tab import Tab
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


@pytest.fixture
def new_tab():
    return {
        'tabId': 1,
        'createdTimestamp': '2019-02-21T14:33:42+00:00',
    }


@pytest.fixture
def create_tab_mutation():
    return '''mutation create_tab($CreateTabInput: CreateTabInput!) {
        createTab(createTabInput: $CreateTabInput) {
            tab {
                tabId
            }
        }
    }'''


@pytest.fixture
def create_tab_post_body(create_tab_mutation, new_tab):
    return {
        'query': create_tab_mutation,
        'variables': {
            'CreateTabInput': new_tab
        },
    }


@pytest.fixture
def saved_tab(new_tab):
    tab = Tab(
        tab_id=new_tab['tabId'],
        created_timestamp=new_tab['createdTimestamp']
    )
    db.session.add(tab)
    db.session.commit()

    return tab


