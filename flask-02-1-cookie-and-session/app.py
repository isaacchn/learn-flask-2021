from flask import Flask, make_response, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = '499d2b6e-d392-43f6-b6cf-5b45ce466c05'


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
        response = '<h1>Hello, %s!</h1>' % name
        if 'logged_in' in session:
            response += '[Authenticated]'
        else:
            response += '[Not Authenticated]'
        return response


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))


if __name__ == '__main__':
    app.run()
