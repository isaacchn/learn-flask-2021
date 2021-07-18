import click
from flask import Flask

app = Flask(__name__)

"""
使用
$ cd flask-01-3-cli
$ flask hello
'Hello, Human!'
"""


@app.cli.command()
def hello():
    click.echo('Hello, Human!')


@app.cli.command("create-user")
@click.argument("name")
def create_user(name):
    click.echo('Create User: ' + name)


@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


if __name__ == '__main__':
    app.run()
