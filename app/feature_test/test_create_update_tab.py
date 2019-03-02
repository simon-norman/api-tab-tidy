import json
import pytest
from app.models.tab import Tab


def call_tab_api(test_client, data):
    return test_client.post(
        '/graphql',
        data=json.dumps(data),
        content_type='application/json'
    )


@pytest.mark.ftest
def test_create_tab(test_client, create_tab_post_body, new_tab):
    response = call_tab_api(test_client, create_tab_post_body)

    saved_tab = Tab.query.all()[0]
    tab_created_time = saved_tab.created_timestamp.isoformat()

    assert tab_created_time == new_tab['createdTimestamp']
    assert saved_tab.tab_id == new_tab['tabId']
    assert 'errors' not in response.json


@pytest.mark.ftest
def test_update_tab(test_client, update_tab_post_body):
    response = call_tab_api(test_client, update_tab_post_body)

    assert 'errors' not in response.json
