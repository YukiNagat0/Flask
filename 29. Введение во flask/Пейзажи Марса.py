from flask import Flask, url_for


app = Flask(__name__)


@app.route('/carousel')
def carousel():
    page = f'''
    <!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                  integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                  crossorigin="anonymous">
            <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
            <script
                src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
                crossorigin="anonymous"></script>
            <title>Пейзажи Марса</title>
        </head>
        <body class="landscapes">
            <h1>
                Пейзажи Марса
            </h1>
            <div id="MarsLandscapes" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#MarsLandscapes" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Слайд 1"></button>
                    <button type="button" data-bs-target="#MarsLandscapes" data-bs-slide-to="1" aria-label="Слайд 2"></button>
                    <button type="button" data-bs-target="#MarsLandscapes" data-bs-slide-to="2" aria-label="Слайд 3"></button>
                </div>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="{url_for('static', filename='img/MarsLandscape1.jpg')}" class="d-block w-100">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/MarsLandscape2.jpg')}" class="d-block w-100">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/MarsLandscape3.jpg')}" class="d-block w-100">
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#MarsLandscapes" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#MarsLandscapes" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </body>
    </html>
    '''
    return page


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
