from flask import Blueprint, render_template
from flask import current_app as app

nameplates_bp = Blueprint('nameplates_bp', __name__, template_folder='templates', static_folder='static')

@nameplates_bp.route('/create', methods=['GET'])
def create_nameplate():
	return 'create nameplate'

@nameplates_bp.route('/nameplates', methods=['GET'])
def nameplates():
	return 'view nameplates'