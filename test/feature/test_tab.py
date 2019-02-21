import pytest
import json
from app import create_app


@pytest.fixture
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    test_client = app.test_client()

    context = app.app_context()
    context.push()

    yield test_client

    context.pop()


create_tab_string = '''mutation create_tab($CreateTabInput: CreateTabInput!) {
    createTab(createTabInput: $CreateTabInput) {
      tab {
        tabId
      }
    }
  }'''

create_tab_body = {
    'query': create_tab_string,
    'variables': {
        'CreateTabInput': {
            'tabId': 1,
            'createdTimestamp': '2019-02-21T14:33:42+00:00',
        }
    },
}


def test_create_tab(test_client):
    response = test_client.post(
        '/graphql', 
        data=json.dumps(create_tab_body),
        content_type='application/json'
    )
    assert response.status_code == 200
    
    
