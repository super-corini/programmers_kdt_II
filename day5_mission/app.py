from flask import Flask
from apis import api
from models import db
import os

app = Flask(__name__)
api.init_app(app)

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'weapon.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)