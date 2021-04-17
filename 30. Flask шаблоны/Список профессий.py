from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof')
@app.route('/list_prof/<list_type>')
def list_prof(list_type=None):
    params = {'title': 'Список профессий'}
    if list_type in {'ol', 'ul'}:
        params['list_type'] = list_type
        params['professions'] = [
            'инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
            'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
            'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов'
        ]
    else:
        params['list_type'] = None

    return render_template('list_prof.html', **params)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
