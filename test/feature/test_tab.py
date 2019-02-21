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


create_tab_string = '''mutation CreateTab($CreateTabInput: CreateTabInput!) {
    createTab(createTabInput: $CreateTabInput) {
      tab {
        tabId
      }
    }
  }'''

create_tab_body = {
    'query': create_tab_string,
    'variables': {
        'create_tab_input': {
            'tab_id': 1,
            'created_timestamp': 'Thu, 21 Feb 2019 14:09:09 GMT',
        }
    },
}


def test_create_tab(test_client):
    # expect that response is 200, for starters
    # create query string
    # create nested dictionary and jsonify it (?) for payload
    print(create_tab_body['query'])
    response = test_client.post(
        '/graphql', 
        data=json.dumps(create_tab_body),
        content_type='application/json'
    )
    print(response)
    
