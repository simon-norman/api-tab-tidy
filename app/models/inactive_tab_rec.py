from app.extensions import db


class InactiveTabRecording(db.Model):
    __tablename__ = 'inactive_tab_recordings'
    tab_id = db.Column(db.Integer, primary_key=True)
    active_timestamp = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    inactive_timestamp = db.Column(db.TIMESTAMP(timezone=True), nullable=False)

    def __repr__(self):
        return '<Tab %r>' % self.id