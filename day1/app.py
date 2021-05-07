from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# db = SQLAlchemy()
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(32), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Menu('{self.id}', '{self.name}', '{self.price}')"

@app.route('/menus/')
def get_menus():
    return jsonify([
        {
            'id': menu.id, 'name': menu.name, 'price': menu.price
        } for menu in Menu.query.all()
    ])

@app.route('/menus/<id>/')
def get_a_menu(id):
    print(id)
    menu = Menu.query.filter_by(id=id).first_or_404()
    return {
        'id':menu.id, 'name':menu.name, 'price':menu.price
    }

# import uuid

@app.route('/menus/',methods=['POST'])
def create_user():
    data = request.get_json()
    # if not 'name' in data or not 'price' in data:
    #     return jsonify({
    #         'error': 'Bad Request',
    #         'message': 'Name or Price is not given'
    #     }), 400
    # if len(data['name'])< 2 or len(data['price']) < 2:
    #     return jsonify({
    #         'error': 'Bad Request',
    #         'message': 'Name or Price must be contain minimum of 3 letters'
    #     }), 400
    
    new_menu = Menu(
        id = data['id'],
        name = data['name'],
        price = data['price']
    )

    db.session.add(new_menu)
    db.session.commit()
    return {
        'id': new_menu.id, 'name': new_menu.name, 'price': new_menu.price
    }, 201

@app.route('/menus/<id>/', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    # if 'name' not in data:
    #     return {
    #         'error': 'Bad Request',
    #         'message':'Name field needs to be present'
    #     }, 400
    menu = Menu.query.filter_by(id=id).first_or_404()
    menu.name = data['name']
    # menu.price = data['price']
    
    db.session.commit()
    return jsonify({
        'id': menu.id,
        'name': menu.name,
        'price': menu.price
    })

@app.route('/menus/<id>/',methods=['DELETE'])
def delete_user(id):
    menu = Menu.query.filter_by(id=id).first_or_404()
    db.session.delete(menu)
    db.session.commit()
    return {
        'success': 'Data deleted successfully'
    }


@app.route('/')
def home():
    return {
        'message': 'Welcome to build RESTful APIs with Flask and SQLAlchemy'
    }, 200

if __name__ == '__main__':
    app.run()