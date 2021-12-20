from flask import Flask, abort, redirect, flash, render_template
from flask_login import login_user, logout_user, login_required
from application import app, db, login_manager
from application.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from application.forms import LoginForm, SignupForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()

		if user:
			if check_password_hash(user.password_hash, form.password.data):
				login_user(user)
				flash('success')
				return redirect('/')

			else:
				flash('Login Failed')
		else:
			flash('Login failed')

	return render_template('login.html', form=form)
    

@app.route('/logout', methods=['GET'])
@login_required
def logout():
	logout_user()
	return redirect('/')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	
	form = SignupForm()

	if form.validate_on_submit():

		user = User.query.filter_by(email=form.email.data).first()
		if user is None:
			hashed_pw = generate_password_hash(form.password.data, "sha256")
			user = User(username=form.username.data, email=form.email.data, password_hash=hashed_pw)
			db.session.add(user)
			db.session.commit()
			flash('User added')
		
	else:
		print('failed to validate')
		

	return render_template('signup.html', form=form)