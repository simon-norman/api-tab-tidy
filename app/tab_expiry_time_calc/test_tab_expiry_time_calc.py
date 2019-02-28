import pytest
import datetime
from .tab_expiry_time_calc import TabExpiryTimeCalc
from unittest.mock import patch, MagicMock


class MockRec:
    def __init__(self, inactive_timestamp, active_timestamp):
        self.inactive_timestamp = inactive_timestamp
        self.active_timestamp = active_timestamp


def create_inactive_rec_data():
    inactive_rec_data = []
    inactive_timestamp = datetime.datetime(2020, 1, 1, 0, 0, 0)
    active_timestamp = datetime.datetime(2020, 1, 1, 0, 0, 30)

    for tab_id in range(0, 500):
        mock_rec = MockRec(inactive_timestamp, active_timestamp)
        inactive_rec_data.append(mock_rec)
    
    return inactive_rec_data


@patch('app.tab_expiry_time_calc.tab_expiry_time_calc.InactiveTabRecording')
@pytest.mark.unittest
def test_calc_expiry_time(MockInactiveTabRec):
    mock_inactive_tab_rec = MagicMock()
    mock_inactive_tab_rec.query.all.return_value = create_inactive_rec_data()
    
    MockInactiveTabRec.return_value = mock_inactive_tab_rec

    tab_expiry_time_calc = TabExpiryTimeCalc()
    assert tab_expiry_time_calc.expiry_time() == 30
