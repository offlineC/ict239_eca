from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, FloatField, HiddenField,DateField
from wtforms.validators import Email, Length, InputRequired, DataRequired

class RegForm(FlaskForm):
	email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'),Length(max=30)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20)])
	name = StringField('Name')

class LogForm(FlaskForm):
	email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'),Length(max=30)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20)])


class bookForm(FlaskForm):
	check_in_date = DateField('check_in_date', [DataRequired()])


