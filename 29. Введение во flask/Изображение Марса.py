from flask import Flask, url_for


app = Flask(__name__)


@app.route('/image_mars')
def image_mars():
    page = f'''
    <!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <figure>
                <img src="{url_for('static', filename='img/mars.png')}" width="300" height="300">
                <figcaption>Вот она какая, красная планета.</figcaption>
            </figure>
        </body>
    </html>
    '''
    return page


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
