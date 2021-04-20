import json

from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return redirect('/gallery')


@app.route('/gallery', methods=['POST', 'GET'])
def gallery():
    params = {
        'title': 'Галерея с загрузкой'
    }
    with open('static/img/marsLandscapes/numberOfLandscapes.json', 'r', encoding='UTF-8') as f:
        number_of_landscapes = json.load(f)

    if request.method == 'POST':
        number_of_landscapes['n'] += 1
        uploaded_file = request.files.get('file')
        uploaded_file.save(f'static/img/marsLandscapes/MarsLandscape{number_of_landscapes["n"]}.jpg')

        with open('static/img/marsLandscapes/numberOfLandscapes.json', 'w', encoding='UTF-8') as f:
            json.dump(number_of_landscapes, f)

    params['n'] = number_of_landscapes['n']
    return render_template('gallery.html', **params)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
