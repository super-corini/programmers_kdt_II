from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db

# from resources.store import Store, StoreList, store_ns, stores_ns
# from resources.item import Item, ItemList, items_ns, item_ns
from resources.weapon import Weapon, WeaponList, Whoami, weapons_ns, Echo, weapon_ns, whoami_ns, echo_ns
from marshmallow import ValidationError

app = Flask(__name__)
# bluePrint = Blueprint('api', __name__, url_prefix='/api')
# api = Api(bluePrint, doc='/doc', title='Sample Flask-RestPlus Application')
# app.register_blueprint(bluePrint)
api = Api(app, version='1.0', title='API Title', description='API Description') # API 만든다
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

# Add namespace
api.add_namespace(weapon_ns)
api.add_namespace(weapons_ns)
api.add_namespace(whoami_ns)
api.add_namespace(echo_ns)
# api.add_namespace(store_ns)
# api.add_namespace(stores_ns)


@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


weapon_ns.add_resource(Weapon, '/<string:name>')
weapons_ns.add_resource(WeaponList, "")
whoami_ns.add_resource(Whoami, "")
echo_ns.add_resource(Echo, "")

# store_ns.add_resource(Store, '/<int:id>')
# stores_ns.add_resource(StoreList, "")

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)