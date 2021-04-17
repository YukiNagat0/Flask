from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/training')
@app.route('/training/<speciality>')
def training(speciality=None):
    params = dict()
    if not speciality:
        params['caption'] = 'Схема коробля'
        params['image'] = url_for('static', filename='img/falcon.png')
    elif 'инженер' in speciality.lower() or 'строитель' in speciality.lower():
        params['caption'] = 'Инженерные тренажеры'
        params['image'] = url_for('static', filename='img/falconEngineer.png')
    else:
        params['caption'] = 'Научные симуляторы'
        params['image'] = url_for('static', filename='img/falconScientist.png')

    return render_template('training.html', **params)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
