from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, NumberRange


class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(message='Это поле обязательно.')])
    password_1 = PasswordField('Password', validators=[DataRequired(message='Это поле обязательно.')])
    password_2 = PasswordField('Repeat password', validators=[EqualTo('password_1', 'Пароли не совпадают.')])
    surname = StringField('Surname', validators=[DataRequired(message='Это поле обязательно.')])
    name = StringField('Name', validators=[DataRequired(message='Это поле обязательно.')])
    age = IntegerField('Age', validators=[DataRequired(message='Возраст должен быть больше нуля.'),
                                          NumberRange(1, message='Возраст должен быть больше нуля.')])
    position = StringField('Position', validators=[DataRequired(message='Это поле обязательно.')])
    speciality = StringField('Speciality', validators=[DataRequired(message='Это поле обязательно.')])
    address = StringField('Address', validators=[DataRequired(message='Это поле обязательно.')])
    submit = SubmitField('Register')
