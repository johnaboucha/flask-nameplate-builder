from werkzeug.security import check_password_hash, generate_password_hash
from application import db
from flask_login import UserMixin
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


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(200), unique=True, nullable=False)
	password_hash = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User %r>' % self.username