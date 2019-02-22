from unittest.mock import MagicMock, patch
from models.tab import Tab
import pytest


@pytest.mark.unittest
@patch('models.tab.SQLAlchemy')
def test_declare_tab_model(sql_alchemy_mock):
    model_mock = MagicMock()
    sql_alchemy_mock.Model = model_mock
    
    column_mock = MagicMock()
    sql_alchemy_mock.column = column_mock
    
    assert column_mock.call_count == 5
