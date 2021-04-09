from flask import Flask, url_for


app = Flask(__name__)


@app.route('/astronaut_selection')
def astronaut_selection():
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
            <title>Отобор астронавтов</title>
        </head>
        <body class="selection">
            <h1>Анкета претендента</h1>
            <h2>на участие в миссии</h2>
            <form class="mb-3">
                <div class="form-group">
                    <input type="text" class="form-control" placeholder="Введите фамилию">
                    <input type="text" class="form-control" placeholder="Введите имя">
                </div>

                <div class="form-group">
                    <input type="email" class="form-control" placeholder="Введите адрес почты">
                </div>

                <div class="form-group">
                    <label class="form-label" for="educationLevelSelect">Какое у Вас образование?</label>
                    <select class="form-control" id="educationLevelSelect">
                        <option>Начальное</option>
                        <option>Среднее</option>
                        <option>Высшее</option>
                    </select>
                </div>

                <div class="form-group">
                    <label class="form-label">Какие у Вас есть профессии?</label>
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="profession1">
                        <label class="form-check-label" for="profession1">
                            Инженер-исследователь
                        </label>
                    </div>

                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="profession2">
                        <label class="form-check-label" for="profession2">
                            Инженер-строитель
                        </label>
                    </div>

                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="profession3">
                        <label class="form-check-label" for="profession3">
                            Пилот
                        </label>
                    </div>

                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="profession4">
                        <label class="form-check-label" for="profession4">
                            Метеоролог
                        </label>
                    </div>

                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="profession5">
                        <label class="form-check-label" for="profession5">
                            Инженер по жизнеобеспечению
                        </label>
                    </div>

                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="profession6">
                        <label class="form-check-label" for="profession6">
                            Инженер по радиационной защите
                        </label>
                    </div>

                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="profession7">
                        <label class="form-check-label" for="profession7">
                            Врач
                        </label>
                    </div>

                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="profession8">
                        <label class="form-check-label" for="profession8">
                            Экзобиолог
                        </label>
                    </div>
                </div>

                <div class="from-group">
                   <label class="form-label">Укажите пол</label>
                    <div class="form-check">
                        <input type="radio" class="form-check-input" id="male" name="sex" checked>
                        <label class="form-check-label" for="male">
                            Мужской
                        </label>
                    </div>

                    <div class="form-check">
                        <input type="radio" class="form-check-input" id="female" name="sex">
                        <label class="form-check-label" for="female">
                            Женский
                        </label>
                    </div>
                </div>

                <div class="form-group">
                    <label class="form-label" for="about">Немного о себе</label>
                    <textarea class="form-control" id="about" rows="3"></textarea>
                </div>

                <div class="form-group">
                    <label class="form-label" for="photo">Приложите фотографию</label>
                    <input type="file" class="form-control" id="photo">
                </div>

                <div class="form-check">
                    <input type="checkbox" class="form-check-input" id="accept">
                    <label class="form-check-label" for="accept">Готовы остаться на Марсе?</label>
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
        </body>
    </html>
    '''
    return page


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
