from unittest.mock import MagicMock, patch
from app.models.tab import Tab
import pytest


@pytest.mark.unittest
@patch('app.extensions.db')
def test_declare_tab_model(db_mock):
    column_mock = MagicMock()
    db_mock.column = column_mock
    
    assert column_mock.call_count == 5
