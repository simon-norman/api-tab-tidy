from unittest.mock import patch
import json
from graphene.test import Client
from .tab_schema import schema
import pytest

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


@pytest.mark.unittest
@patch('app.graphql_schemas.tab_schema.TabModel')
def test_creates_new_tab_model(TabModelMock):
    client = Client(schema)
    result = client.execute(json.dumps(create_tab_post_body))
    
    assert TabModelMock.call_count == 1
