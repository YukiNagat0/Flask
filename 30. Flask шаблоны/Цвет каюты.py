from typing import Tuple

from flask import Flask, render_template, url_for, redirect
from colorsys import rgb_to_hsv, hsv_to_rgb

app = Flask(__name__)

BASE_COLORS = {
    'male': (0, 0, 255),
    'female': (255, 0, 0)
}


def change_color_saturation(r: float, g: float, b: float, factor: float) -> Tuple[float, float, float]:
    h, s, v = rgb_to_hsv(r, g, b)
    s = factor
    r, g, b = hsv_to_rgb(h, s, v)
    return r, g, b


def get_hex_from_rgb(r: float, g: float, b: float) -> str:
    return f"#{'%02x%02x%02x' % tuple(map(int, (r, g, b)))}"


@app.route('/')
@app.route('/index')
def index():
    return redirect('/table')


@app.route('/table')
@app.route('/table/<gender>')
@app.route('/table/<gender>/<age>')
def table(gender=None, age: str=None):
    params = {
        'title': 'Цвет каюты'
    }

    if gender and age and gender in {'male', 'female'} and age.isdigit():
        age = int(age)
        factor = min(1.0, age / 100)
        params['color'] = get_hex_from_rgb(*change_color_saturation(*BASE_COLORS[gender], factor))
        params['image'] = url_for('static', filename='img/child.jpg') if age < 21 else url_for('static',
                                                                                               filename='img/adult.jpg')
    else:
        params['color'] = None
        params['image'] = None

    return render_template('table.html', **params)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
