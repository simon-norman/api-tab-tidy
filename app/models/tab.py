from app.extensions import db


class Tab(db.Model):
    __tablename__ = 'tabs'
    tab_id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    last_active_timestamp = db.Column(db.TIMESTAMP(timezone=True))
    closed_timestamp = db.Column(db.TIMESTAMP(timezone=True))
    window_id = db.Column(db.String(120))

    def __repr__(self):
        return '<Tab %r>' % self.id
