from application import db
from datetime import datetime

class Nameplates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    photo = db.Column(db.String(200), nullable=True)  
    hours = db.Column(db.String(200), nullable=False)
    department = db.Column(db.String(200), nullable=False)
    college = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Nameplate %r>' % self.id