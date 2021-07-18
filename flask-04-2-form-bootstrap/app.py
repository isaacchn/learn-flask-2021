from flask import Flask, render_template
import os

from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/basic')
def basic():
    form = LoginForm()
    return render_template('bootstrap.html', form=form)


if __name__ == '__main__':
    app.run()
