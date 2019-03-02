import json
import pytest
from app.models.inactive_rec import InactiveRec


def call_tab_api(test_client, data):
    return test_client.post(
        '/graphql',
        data=json.dumps(data),
        content_type='application/json'
    )


@pytest.mark.ftest
def test_create_inactive_rec(
    test_client,
    new_inactive_rec,
    create_inactive_rec_body
):
    response = call_tab_api(test_client, create_inactive_rec_body)

    saved_rec = InactiveRec.query.all()[0]
    saved_active_time = saved_rec.active_timestamp.isoformat()
    saved_inactive_time = saved_rec.inactive_timestamp.isoformat()

    assert saved_inactive_time == new_inactive_rec['inactiveTimestamp']
    assert saved_active_time == new_inactive_rec['activeTimestamp']
    assert 'errors' not in response.json
