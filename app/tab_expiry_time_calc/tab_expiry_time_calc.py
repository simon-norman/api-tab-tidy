from app.models.inactive_tab_rec import InactiveTabRecording
from statistics import mean


class TabExpiryTimeCalc:
    def __init__(self):
        self.inactive_tab_rec = InactiveTabRecording()

    def expiry_time(self):
        inactive_recs = self.inactive_tab_rec.query.all()
        inactive_times = []

        for rec in inactive_recs:
            inactive_time = rec.active_timestamp - rec.inactive_timestamp 
            inactive_times.append(inactive_time.seconds)

        return mean(inactive_times)
