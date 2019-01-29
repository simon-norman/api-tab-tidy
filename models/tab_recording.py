from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TabRecording(db.Model):
    __tablename__ = 'tab_recordings'
    id = db.Column(db.Integer, primary_key=True)
    tab_id = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Enum("active", "inactive", name="status_enum", create_type=False, nullable=False))
    in_use = db.Column(db.Boolean, nullable=False)
    last_timestamp_active = db.Column(db.DateTime, nullable=False)
    secs_since_active = db.Column(db.Integer, nullable=False)
    window_id = db.Column(db.String(120))

    def __repr__(self):
        return '<Tab %r>' % self.id
