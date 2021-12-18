

class Config:
	SECRET_KEY = 'adsfl4890u498hfaiuhef98hf'
	FLASK_ENV = 'development'
	FLASK_APP = 'wsgi.py'

	STATIC_FOLDER = 'static'
	TEMPLATES_FOLDER = 'templates'
	UPLOAD_FOLDER = 'uploads'
	MAX_CONTENT_LENGTH = 2 * 1000 * 1000 # 2MB max upload size

	SQLALCHEMY_DATABASE_URI = 'sqlite:///nameplates.db'