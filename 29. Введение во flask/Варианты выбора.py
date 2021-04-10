import random
from flask import Flask, url_for


app = Flask(__name__)

PLANETS = {
    'Марс': [
        'Эта планета близка к Земле;',
        'На ней много необходимых ресурсов;',
        'На ней есть вода и атмосфера;',
        'На ней есть небольшое магнитное поле;',
        'Наконец, она просто красива!'
    ],
    'Меркурий': [
        'Эта планета ближайшая к Солнцу;',
        'Наименьшая из планет земной группы;',
        'Самая быстрая планета по времени оборота вокруг Солнца;',
        'Обладает небольшим магнитным полем;',
        'Давление ее атмосфера в 5*10^11 меньше Земного'
    ],
    'Венера': [
        'Вторая планета по удалённости от Солнца;',
        'Шестая по размеру планета Солнечной системы;',
        'У Венеры нет магнитного поля;',
        'Температура ее поверхности составляяет 470 градусов цельсия'
    ]
}

ALERT_TYPES = ['alert-primary', 'alert-secondary', 'alert-success',
               'alert-danger', 'alert-warning', 'alert-info', 'alert-light', 'alert-dark']


@app.route('/choice/<planet>')
def choice(planet):
    if planet in PLANETS:
        planet_description_lines = '\n'.join((
            f'''<div class="alert {random.choice(ALERT_TYPES)}" role="alert">
                    {planet_description_line}
                </div>''' for planet_description_line in PLANETS[planet]
        ))

        page = f'''
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <link rel="stylesheet"
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                crossorigin="anonymous">
                <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                <title>Варианты выбора</title>
            </head>
            <body>
                <h1>Мое предложение: {planet}</h1>
                
                {planet_description_lines}
                
            </body>
        </html>
        '''
    else:
        page = f'''
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <link rel="stylesheet"
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                crossorigin="anonymous">
                <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                <title>Варианты выбора</title>
            </head>
            <body>
                <div class="alert alert-danger" role="alert">
                    Пока описания доступны только для планет земной группы: Марс, Меркурий, Венера.
                </div>
            </body>
        </html> 
        '''
    return page


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
