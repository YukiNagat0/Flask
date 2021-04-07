from flask import Flask, url_for


app = Flask(__name__)


@app.route('/promotion_image')
def promotion_image():
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
            <title>Колонизация</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='img/mars.png')}" width="300" height="300">
            <div class="alert alert-secondary" role="alert">
                Человечество вырастает из детства.
            </div>
            <div class="alert alert-success" role="alert">
                Человечеству мала одна планета.
            </div>
            <div class="alert alert-secondary" role="alert">
                Мы сделаем обитаемыми безжизненные пока планеты.
            </div>
            <div class="alert alert-warning" role="alert">
                И начнем с Марса!
            </div>
            <div class="alert alert-danger" role="alert">
                Присоединяйся!
            </div>
        </body>
    </html>
    '''
    return page


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
