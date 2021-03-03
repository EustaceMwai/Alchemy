from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eustace.db'
engine = create_engine("sqlite:///eustace.db")
session = scoped_session(sessionmaker(bind=engine))
db = SQLAlchemy(app)


@app.teardown_request
def remove_session(ex=None):
    session.remove()


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Employee %r> ' % self.name
