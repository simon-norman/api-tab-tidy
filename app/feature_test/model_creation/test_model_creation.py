import pytest


@pytest.mark.ftest
def test_model_created(tab_db_with_test_data):
    result = 1 + 1

    # initialise test db and inject data
    # call generate model
    # test that model file created - just that it exists

