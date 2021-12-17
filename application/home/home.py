from flask import Blueprint, render_template
from flask import current_app as app

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/home-static')

@home_bp.route('/', methods=['GET'])
def home():
	"""Homepage."""
	return render_template('homepage.html')

@home_bp.route('/about', methods=['GET'])
def about():
	"""Homepage."""
	return 'about page'