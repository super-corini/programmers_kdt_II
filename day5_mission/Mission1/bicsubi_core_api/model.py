from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+dbfile

db = SQLAlchemy(app)

class Weapon(db.Model):
    __tablename__="Weapon"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    stock = db.Column(db.Integer, nullable=False)