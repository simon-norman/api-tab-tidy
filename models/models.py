from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tab(db.Model):
    __tablename__ = 'tabs'
    tab_id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False)
    last_active_timestamp = db.Column(db.DateTime)
    closed_timestamp = db.Column(db.DateTime)
    window_id = db.Column(db.String(120))

    def __repr__(self):
        return '<Tab %r>' % self.id
