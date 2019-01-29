from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tab(db.Model):
    __tablename__ = 'tabs'
    id = db.Column(db.String(120), primary_key=True)
    status = db.Column(db.Enum("live", "dead", name="status_enum", create_type=False))
    secs_since_tab_active = db.Column(db.Integer)
    window_id = db.Column(db.String(120))

    def __repr__(self):
        return '<Tab %r>' % self.id
