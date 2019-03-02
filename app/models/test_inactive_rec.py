import pytest
from .inactive_rec import InactiveRec


@pytest.mark.unittest
def test_create_inactive_tab_rec(saved_tab, test_tab_db):
    inactive_timestamp = '2019-02-21T15:35:42+00:00'
    active_timestamp = '2019-02-21T15:35:42+00:00'

    inactive_tab_rec = InactiveRec(
        tab_id=saved_tab.tab_id,
        active_timestamp=active_timestamp,
        inactive_timestamp=inactive_timestamp,
    )
    test_tab_db.session.add(inactive_tab_rec)
    test_tab_db.session.commit()

    saved_rec = InactiveRec.query.get(inactive_tab_rec.id)

    assert saved_rec.tab_id == inactive_tab_rec.tab_id


@pytest.mark.unittest
def test_get_all_inactive_rec(saved_inactive_tab_recs):
    inactive_tab_recs = InactiveRec.query.all()

    assert len(inactive_tab_recs) == len(saved_inactive_tab_recs)
