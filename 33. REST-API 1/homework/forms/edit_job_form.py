from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional


class EditJobForm(FlaskForm):
    job = StringField('Job title', validators=[DataRequired('Это поле обязательно')])

    # Пришлось сделать это поле опциональным. Вся проверка этого поля происходит в main'e.
    # Причины: обычный юзер может ставить только свой id в качестве team_leader_id. У него это поле disabled
    # поэтому, value не отправляется на сервер. А на это ругается и IntegerField и DataRequired и NumberRange
    # поэтому пришлось сделать вот так:
    team_leader_id = StringField('Team leader id', validators=[Optional()])

    work_size = IntegerField('Work size', validators=[
        DataRequired('Количество часов должно быть больше либо равно нуля.'),
        NumberRange(0, message='Количество часов должно быть больше либо равно нуля.')])

    collaborators = StringField('Collaborators ids', validators=[DataRequired('Это поле обязательно.')])
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Add')
