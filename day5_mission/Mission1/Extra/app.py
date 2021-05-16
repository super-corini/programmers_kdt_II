import os

from flask import Flask
from flask_restx import Api

from bicsubi import Bicsubi
from weapon import Weapons
from models import db

app = Flask(__name__)
api = Api(
    app,
    version = '0.1',
    title = 'Bicsubi',
    description = 'Programmers DevCourse Week4 Bicsubi'
)

base_dir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(base_dir, 'weapons.sqlite')

app.config['SECREY_KEY'] = 'ProgrammersDevCourse'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

db.init_app(app)
db.app = app
db.create_all()


api.add_namespace(Bicsubi, path='')
api.add_namespace(Weapons, '/weapons')


if __name__ == "__main__" :
    app.run(debug=True)
