from flask import Flask, render_template, url_for

app = Flask(__name__)


FORM = {
    'Фамилия': 'Watny',
    'Имя': 'Mark',
    'Образование': 'выше среднего',
    'Профессия': 'штурман марсохода',
    'Пол': 'male',
    'Мотивация': 'Всегда мечтал застряять на Марсе!',
    'Готовы остаться на Марсе?': True,
}


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {
        'style_path': url_for('static', filename='css/style.css'),
        'title': 'Анкета',
        'form': FORM
    }
    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
