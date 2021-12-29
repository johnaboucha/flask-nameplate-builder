from flask import render_template
from application import app
from application.models import Nameplate, User
from flask_login import login_required, current_user


@app.template_filter('make_date')
def my_date(text):
	"""Convert timestamp to nice date."""
	return text.strftime("%B %d, %Y")




@app.route("/profile")
@login_required
def user_profile():
	user_id = current_user.get_id()
	user = User.query.get(user_id)

	nameplates = Nameplate.query.filter_by(created_by=user_id).order_by(Nameplate.date_created).all()

	context = {
		'user': user,
		'nameplates': nameplates,
	}

	return render_template('user_profile.html', **context)