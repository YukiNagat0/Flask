import json

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return redirect('/member')


@app.route('/member')
def member():
    params = {
        'title': 'Личная карточка'
    }

    with open('templates/members.json', 'r', encoding='UTF-8') as members_json:
        members = json.load(members_json)

    params['members'] = members

    return render_template('member.html', **params)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
