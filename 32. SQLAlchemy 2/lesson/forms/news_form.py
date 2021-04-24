from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Содержиание')
    is_private = BooleanField('Личное')
    submit = SubmitField('Применить')
