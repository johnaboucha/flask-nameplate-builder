from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Global libraries
db = SQLAlchemy()

def init_app():
	"""Create Flask application."""
	app = Flask(__name__, instance_relative_config=False)
	app.config.from_object('config.Config')

	# Initialize Plugins
	db.init_app(app)

	with app.app_context():
		# Import routes
		from .home import home
		from .nameplates import nameplates

		# Register Blueprints
		app.register_blueprint(home.home_bp)
		app.register_blueprint(nameplates.nameplates_bp)

		return app