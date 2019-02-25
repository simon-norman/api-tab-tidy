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

    assert saved_tab.created_timestamp.isoformat() == new_tab['createdTimestamp']
    assert saved_tab.tab_id == new_tab['tabId']
    assert 'errors' not in response.json


update_tab_mutation = '''mutation update_tab($UpdateTabInput: UpdateTabInput!) {
    updateTab(updateTabInput: $UpdateTabInput) {
      tab {
        tabId
      }
    }
  }'''

update_tab_post_body = {
    'query': update_tab_mutation,
    'variables': {
        'UpdateTabInput': ''
    },
}


@pytest.mark.ftest
def test_update_tab(test_client, saved_tab):
    updated_tab = {
        'tabId': saved_tab.tab_id,
        'closedTimestamp': '2021-02-21T16:33:42+00:00',
        'lastActiveTimestamp': '2020-10-21T14:33:42+00:00'
    }
    update_tab_post_body['variables']['UpdateTabInput'] = updated_tab
    response = call_tab_api(test_client, update_tab_post_body)

    assert 'errors' not in response.json
    
    
