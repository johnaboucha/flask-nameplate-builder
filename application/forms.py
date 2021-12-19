from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Length

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