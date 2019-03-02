from app.models.inactive_tab_rec import InactiveTabRecording
from statistics import mean


class TabExpiryTimeCalc:
    def __init__(self):
        self.inactive_tab_rec = InactiveTabRecording()

    def expiry_time(self):
        inactive_times = []
        for rec in self.get_inactive_recs():
            inactive_times.append(self.calc_inactive_time(rec))

        return mean(inactive_times)

    def get_inactive_recs(self):
        return self.inactive_tab_rec.query.all()

    def calc_inactive_time(self, rec):
        inactive_time = rec.active_timestamp - rec.inactive_timestamp
        return inactive_time.seconds

