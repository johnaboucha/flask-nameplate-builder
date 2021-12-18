from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, login_required
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, SignupForm
from application import db
from application.models import Users

login_bp = Blueprint('login_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/login-static')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = Users.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password_hash, form.password.data):
				login_user(user)
				return redirect(url_for('login_bp.profile'))
			else:
				flash("Login failed")
				return redirect(url_for('login_bp.login'))
		else:
			flash("Login failed")
			return redirect(url_for('login_bp.login'))

	return render_template('login.html', form=form)



@login_bp.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()

	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()

		if user is None:
			hashed_pw = generate_password_hash(form.password.data, "sha256")
			user = Users(
				username = form.username.data,
				email=form.email.data,
				password_hash=hashed_pw
			)
			try:
				db.session.add(user)
				db.session.commit()
			except:
				flash("Somthing went wrong")
				return render_template('signup.html', form=form)

			flash("Account Created")
			return redirect(url_for('login_bp.login'))
		else:
			form = SignupForm()
			flash("User already exists")
			return render_template('signup.html', form=form)

	return render_template('signup.html', form=form)


@login_bp.route('/profile', methods=['GET'])
@login_required
def profile():
	return render_template('profile.html')
