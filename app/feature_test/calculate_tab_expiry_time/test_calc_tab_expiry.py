import pytest


@pytest.mark.ftest
def test_model_created(tab_db_with_test_tab_data, tab_expiry_time_calc):
    expiry_time = tab_expiry_time_calc.calc_expiry_time()
    
    assert expiry_time == 60
