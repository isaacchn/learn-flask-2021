from flask import Flask

app = Flask(__name__)

"""
使用
$ cd flask-01-2-shell
$ flask shell
>>> app.name
'app'
"""


@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


if __name__ == '__main__':
    app.run()
