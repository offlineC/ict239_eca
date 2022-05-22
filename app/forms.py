from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, FloatField, HiddenField,DateField
from wtforms.validators import Email, Length, InputRequired, DataRequired

''' 
Question 2) a) 
This copde works by creating a class that reads the inputs of a form in a page when it is called. The primary function spec of these classes is toe check for validation of all inputs, depending on which class is called accordingly for each form. 
Those fields that has InputRequired or DataRequired helps to check if the input has been assigned any values.
'''

class RegForm(FlaskForm):
	email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'),Length(max=30)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20)])
	name = StringField('Name')

class LogForm(FlaskForm):
	email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'),Length(max=30)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20)])


class bookForm(FlaskForm):
	check_in_date = DateField('check_in_date', [DataRequired()])


