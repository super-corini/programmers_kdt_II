from flask import Flask
from flask_restx import Api
from bicsubi import Bicsubi
from weapon_CRUD import Weapon


app = Flask(__name__)
api = Api(app)

api.add_namespace(Bicsubi, path='')
api.add_namespace(Weapon, path='/weapons')


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
