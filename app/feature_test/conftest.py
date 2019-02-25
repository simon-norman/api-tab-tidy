from app.app import create_app
from app.extensions import db
from app.models.tab import Tab
import pytest


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


def generate_tab_mutation_string(mutation_action):
    action_lower = mutation_action.lower()

    return '''mutation {action}_tab(${action}TabInput: {action}TabInput!) {{
        {action_lower}Tab({action_lower}TabInput: ${action}TabInput) {{
            tab {{
                tabId
            }}
        }}
    }}'''.format(action=mutation_action, action_lower=action_lower)


@pytest.fixture(scope="module")
def new_tab():
    return {
        'tabId': 1,
        'createdTimestamp': '2019-02-21T14:33:42+00:00',
    }


@pytest.fixture(scope="module")
def create_tab_post_body(new_tab):
    create_tab_mutation = generate_tab_mutation_string('Create')
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


@pytest.fixture
def updated_tab_to_be_saved(saved_tab):
    return {
        'tabId': saved_tab.tab_id,
        'closedTimestamp': '2021-02-21T16:33:42+00:00',
        'lastActiveTimestamp': '2020-10-21T14:33:42+00:00'
    }

@pytest.fixture
def update_tab_post_body(updated_tab_to_be_saved):
    update_tab_mutation = generate_tab_mutation_string('Update')
    return {
        'query': update_tab_mutation,
        'variables': {
            'UpdateTabInput': updated_tab_to_be_saved
        },
    }
