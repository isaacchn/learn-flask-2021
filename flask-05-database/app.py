from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'foo.db'))

if __name__ == '__main__':
    app.run()

"""
使用flask shell初始化sqlite数据库
$ flask shell
>>> from app import db
>>> db.create_all()

查看建表语句
$ flask shell
>>> from sqlalchemy.schema import CreateTable
>>> from app import Note
>>> print(CreateTable(Note.__table__))

CREATE TABLE note (
        id INTEGER NOT NULL,
        body TEXT,
        PRIMARY KEY (id)
)

--> Create

>>> from app import db
>>> note1 = Note(body='remember Sammy Jankis')
>>> note2 = Note(body='The Three-Body Problem')
>>> db.session.add(note1)
>>> db.session.add(note2)
>>> db.session.commit()

--> Query

>>> Note.query.get(1).body
'remember Sammy Jankis'

--> Update

>>> note=Note.query.get(1)
>>> note.body
'remember Sammy Jankis'
>>> note.body='Double'
>>> db.session.commit()
>>> Note.query.get(1).body
'Double'

--> Delete

>>> note=Note.query.get(1)
>>> db.session.delete(note)
>>> db.session.commit()
>>>
>>>
>>> Note.query.all()
[<Note 2>]
>>> Note.query.first().body
'The Three-Body Problem'
"""


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
