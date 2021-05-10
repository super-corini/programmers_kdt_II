from flask import Flask, jsonify, request
import database
import models


app = Flask(__name__)
db_session = database.db_session
database.init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def hello_flask():
    return 'Hello World'

# /menus CREATE, READ
@app.route('/menus', methods=['GET', 'POST'])
def menu_CR():
    if request.method == 'GET':
        menus = models.Menu.query.all()
        return jsonify({"Menu": menus})
    else:
        request_data = request.get_json()
        
        menu = models.Menu(request_data["name"], request_data["price"])
        db_session.add(menu)
        db_session.commit()
        
        newly_added_menu = models.Menu.query.filter_by(name=request_data["name"]).first()
        return jsonify(newly_added_menu)

# /menus UPDATE DELETE
@app.route('/menus/<int:id>', methods=['PUT', 'DELETE'])
def menu_UD(id):
    menu = models.Menu.query.get(id)

    if request.method == 'PUT':
        request_data = request.get_json()
        menu.name = request_data["name"]
        menu.price = request_data["price"]
        db_session.commit()
        return jsonify(menu)
    else:
        db_session.delete(menu)
        db_session.commit()
        menus = models.Menu.query.all()
        return jsonify({"Menu": menus})


if __name__ == "__main__":
    app.run()
