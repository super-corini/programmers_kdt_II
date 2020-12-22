import os
from flask import Flask, jsonify, request, abort
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import (db, Menu)
from serializer import MenuSchema


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eon:eon@localhost/coffee'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def hello_flask():
    return "Hello COFFEE!"

def query_serializer(schema, query_result):
    ret = []
    for result in query_result:
        ret.append(schema.dump(result))
    return ret


class Menus(Resource):
    def get(self):
        menus_data = Menu.query.all()
        return jsonify(query_serializer(MenuSchema(),menus_data))

    def post(self):
        data = request.get_json()
        try :
            name = data['name']
            price = data['price']
        except Exception as e:
            print(e)
            abort(400)
        
        try:
            new_menu = Menu(name, price)
            db.session.add(new_menu)
            db.session.commit()
        except Exception as e:
            abort(500, e)
        
        return jsonify({"message": "Add successfully!"})

    def put(self, id):
        request_data = request.get_json()
        menu = Menu.query.filter_by(id=id).first()
        if not menu:
            abort(400, 'Not existed!')
        menu.name = request_data['name']
        menu.price = request_data['price']
        db.session.commit()
        return jsonify({"message": "Update successfully!"})

    def delete(self, id):
        menu = Menu.query.filter_by(id=id).first()
        if not menu:
            abort(400, 'Not existed!')
        db.session.delete(menu)
        db.session.commit()
        return jsonify({"message": "Delete successfully!"})


api.add_resource(Menus, '/menu', '/menu/<id>')


if __name__ == '__main__':
    app.run()