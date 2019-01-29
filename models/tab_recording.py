from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TabRecording(db.Model):
    __tablename__ = 'tab_recordings'
    id = db.Column(db.Integer, primary_key=True)
    tabid = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Enum("active", "inactive", name="status_enum", create_type=False, nullable=False))
    in_use = db.Column(db.Boolean)
    last_timestamp_active = db.Column(db.DateTime)
    secs_since_active = db.Column(db.Integer)
    window_id = db.Column(db.String(120))

    def __repr__(self):
        return '<Tab %r>' % self.id
