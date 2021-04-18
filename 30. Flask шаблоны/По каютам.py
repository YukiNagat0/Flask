from flask import Flask, render_template

app = Flask(__name__)

ASTRONAUTS = ['Ридл скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']


@app.route('/distribution')
def distribution():
    params = {
        'title': 'По каютам!',
        'astronauts': ASTRONAUTS
    }

    return render_template('distribution.html', **params)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
