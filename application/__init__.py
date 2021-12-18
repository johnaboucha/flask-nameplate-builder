from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

# Global libraries
db = SQLAlchemy()
login_manager = LoginManager()

def init_app():
	"""Create Flask application."""
	app = Flask(__name__, instance_relative_config=False)
	app.config.from_object('config.Config')

	# Initialize Plugins
	db.init_app(app)
	login_manager.init_app(app)
	login_manager.login_view = 'login_bp.login'

	@login_manager.user_loader
	def load_user(user_id):
		return '' #Users.query.get(int(user_id))

	with app.app_context():
		# Import routes
		from .home import home
		from .nameplates import nameplates
		from .login import login

		# Register Blueprints
		app.register_blueprint(home.home_bp)
		app.register_blueprint(nameplates.nameplates_bp)
		app.register_blueprint(login.login_bp)

		return app