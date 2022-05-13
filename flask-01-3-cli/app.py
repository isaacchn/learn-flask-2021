import click
from flask import Flask

app = Flask(__name__)


@app.cli.command()
def hello():
    """
    使用
    $ cd flask-01-3-cli
    $ flask hello
    'Hello, Human!'
    """
    click.echo('Hello, Human!')


@app.cli.command("create-user")
@click.argument("name")
def create_user(name):
    """
    使用
    $ cd flask-01-3-cli
    $ flask create-user isaac
    Create User: isaac
    """
    click.echo('Create User: ' + name)


@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


if __name__ == '__main__':
    app.run()
