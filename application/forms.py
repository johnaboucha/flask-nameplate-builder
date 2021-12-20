from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms import validators
from wtforms.validators import DataRequired, Length, EqualTo

class NameplateForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired(), Length(max=200)])
	slug = StringField("Slug", validators=[DataRequired(), Length(max=200)])
	title = StringField("Title", validators=[DataRequired(), Length(max=200)])
	email = StringField("Email", validators=[DataRequired(), Length(max=200)])
	phone = StringField("Phone", validators=[Length(max=15)])   
	hours = StringField("Hours", validators=[DataRequired(), Length(max=200)])
	photo = FileField("Photo")
	department = StringField("Department", validators=[DataRequired(), Length(max=200)])
	college = StringField("College", validators=[DataRequired(), Length(max=200)])
	submit = SubmitField("Save")


class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(max=200)])
	password = PasswordField("Passord", validators=[DataRequired(), Length(max=128)])
	submit = SubmitField("Login")

class SignupForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(max=200)])
	password = PasswordField("Password", validators=[DataRequired(), Length(max=128), EqualTo('password_confirm', 'Passwords must match.')])
	password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(max=128)])
	email = StringField("Email", validators=[DataRequired(), Length(max=128)]) 
	submit = SubmitField("Signup")