from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms import validators
from wtforms.validators import DataRequired, Length
from wtforms.fields.simple import PasswordField

# Login Form
class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(max=20, message="Username cannot be more than 20 characters")])
	password = PasswordField("Password", validators=[DataRequired(), Length(max=128, message="Password cannot be more than 128 characters")])
	submit = SubmitField("Login")

# Signup Form
class SignupForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(max=20, message="Username cannot be more than 20 characters")])
	email = StringField("Email", validators=[DataRequired(), Length(max=128, message="Email cannot be more than 128 characters")])
	password = PasswordField("Password", validators=[DataRequired(), Length(max=128, message="Password cannot be more than 128 characters")])
	submit = SubmitField("Signup")