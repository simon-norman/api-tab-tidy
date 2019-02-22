import json
import pytest


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
        'CreateTabInput': {
            'tabId': 1,
            'createdTimestamp': '2019-02-21T14:33:42+00:00',
        }
    },
}


@pytest.mark.ftest
def test_create_tab(test_client):
    response = test_client.post(
        '/graphql', 
        data=json.dumps(create_tab_post_body),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    
    
