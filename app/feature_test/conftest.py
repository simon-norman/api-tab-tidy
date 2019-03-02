import pytest


@pytest.fixture(scope="module")
def create_tab_post_body(new_tab):
    create_tab_mutation = tab_mutation_string('Create')
    return {
        'query': create_tab_mutation,
        'variables': {
            'CreateTabInput': new_tab
        },
    }


def tab_mutation_string(mutation_action):
    action_lower = mutation_action.lower()

    return '''mutation {action}_tab(${action}TabInput: {action}TabInput!) {{
        {action_lower}Tab({action_lower}TabInput: ${action}TabInput) {{
            tab {{
                tabId
            }}
        }}
    }}'''.format(action=mutation_action, action_lower=action_lower)


@pytest.fixture
def updated_tab_to_be_saved(saved_tab):
    return {
        'tabId': saved_tab.tab_id,
        'closedTimestamp': '2021-02-21T16:33:42+00:00',
        'lastActiveTimestamp': '2020-10-21T14:33:42+00:00'
    }


@pytest.fixture
def update_tab_post_body(updated_tab_to_be_saved):
    update_tab_mutation = tab_mutation_string('Update')
    return {
        'query': update_tab_mutation,
        'variables': {
            'UpdateTabInput': updated_tab_to_be_saved
        },
    }


@pytest.fixture
def new_inactive_rec(saved_tab):
    return {
        'tabId': saved_tab.tab_id,
        'inactiveTimestamp': '2020-01-01T00:00:00+00:00',
        'activeTimestamp': '2020-01-01T00:00:30+00:00'
    }


@pytest.fixture
def create_inactive_rec_body(new_inactive_rec):
    create_inactive_rec_mutation = inactive_rec_mutation_string('Create')
    return {
        'query': create_inactive_rec_mutation,
        'variables': {
            'CreateInactiveRecInput': new_inactive_rec
        },
    }


def inactive_rec_mutation_string(mutation_action):
    action_lower = mutation_action.lower()

    return '''mutation {action}_inactive_rec(${action}InactiveRecInput: {action}InactiveRecInput!) {{
        {action_lower}InactiveRec({action_lower}InactiveRecInput: ${action}InactiveRecInput) {{
            inactiveRec {{
                id
            }}
        }}
    }}'''.format(action=mutation_action, action_lower=action_lower)
