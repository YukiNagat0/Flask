from flask import Flask, request, url_for
import base64

app = Flask(__name__)

IMAGE_TYPES = {
    '.jpg': 'jpeg',
    '.jpeg': 'jpeg',
    '.png': 'png'
}


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    allowed_extensions = ','.join(IMAGE_TYPES.keys())
    if request.method == 'GET':
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
                
                <title>Отбор астронавтов</title>
            </head>
            <body class="image_upload">
                <h1>Загрузка фотографии</h1>
                <h2>для участия в миссии</h2>
                <div>
                    <form class="image_upload_form" method="post" enctype="multipart/form-data">
                        <div class="mb-3">
                            <label for="photo" class="form-label">Приложите фотографию</label>
                            <input type="file" accept={allowed_extensions} class="form-control" id="photo" name="image">
                        </div>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </div>
            </body>
        </html>
        '''
    elif request.method == 'POST':
        file_object = request.files.get('image')
        image_filename = file_object.filename
        image_extension = image_filename[image_filename.rfind('.'):]
        bs64 = base64.encodebytes(file_object.read()).decode('UTF-8')
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
                
                <title>Отбор астронавтов</title>
            </head>
            <body class="image_upload">
                <h1>Загрузка фотографии</h1>
                <h2>для участия в миссии</h2>
                <div>
                    <form class="image_upload_form" method="post" enctype="multipart/form-data">
                        <div class="mb-3">
                            <label for="photo" class="form-label">Приложите фотографию</label>
                            <input type="file" accept={allowed_extensions} class="form-control" id="photo" name="image">
                        </div>
                        <img src="data:image/{image_extension};base64,{bs64}" width="400" height="400">
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </div>
            </body>
        </html>
        '''
    else:
        page = "Что-то пошло не так."
    return page


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
