from flask import Flask, url_for


app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname: str, level: int, rating: float):
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
            <title>Результаты</title>
        </head>
        <body>
            <h1>Результаты отбора</h1>
            <h2>Претендента на участие в миссии {nickname}:</h2>
            <div class="alert alert-success" role="alert">
                Поздравляем! Ваш рейтинг после {level} этапа отбора
            </div>
            <div class="alert alert-light" role="alert">
                составляет {rating}!
            </div>
            <div class="alert alert-warning" role="alert">
                Желаем удачи!
            </div>
        </body>
    </html>
    '''
    return page


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
