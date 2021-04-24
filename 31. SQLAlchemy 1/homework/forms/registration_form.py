from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, NumberRange


class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password_1 = PasswordField('Password', validators=[DataRequired()])
    password_2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password_1')])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(0)])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')
