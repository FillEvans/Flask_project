from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'aopsdkopvbji349-igfdkmjvlkxcmv0-23-02'
db = SQLAlchemy(app)
manager = LoginManager(app)

from app import models, routes


with app.app_context():
    db.create_all()
