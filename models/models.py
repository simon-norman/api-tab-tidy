from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tab(db.Model):
    __tablename__ = 'tabs'
    id = db.Column(db.Integer, primary_key=True)
    last_timestamp_active = db.Column(db.DateTime)
    window_id = db.Column(db.String(120))

class TabRecording(db.Model):
    __tablename__ = 'tab_recordings'
    id = db.Column(db.Integer, primary_key=True)
    tab_id = db.Column(db.String(120), db.ForeignKey('tab.id'), nullable=False)
    status = db.Column(db.Enum("active", "inactive", name="status_enum", create_type=False, nullable=False))
    in_use = db.Column(db.Boolean)
    timestamp_recorded = db.Column(db.DateTime, nullable=False)
    secs_since_active = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Tab %r>' % self.id
