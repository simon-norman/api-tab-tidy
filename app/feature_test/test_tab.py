import json
import pytest
from app.models.tab import Tab

tab = {
    'tabId': 1,
    'createdTimestamp': '2019-02-21T14:33:42+00:00',
}

create_tab_mutation = '''mutation create_tab($CreateTabInput: CreateTabInput!) {
    createTab(createTabInput: $CreateTabInput) {
      tab {
        tabId
      }
    }
  }'''

create_tab_post_body = {
    'query': create_tab_mutation,
    'variables': {
        'CreateTabInput': tab
    },
}


@pytest.mark.ftest
def test_create_tab(test_client):
    response = test_client.post(
        '/graphql', 
        data=json.dumps(create_tab_post_body),
        content_type='application/json'
    )

    saved_tab = Tab.query.all()[0]

    assert saved_tab.created_timestamp.isoformat() == tab['createdTimestamp']
    assert saved_tab.tab_id == tab['tabId']
    assert 'errors' not in response.json
    
    
