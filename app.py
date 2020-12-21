from flask import Flask, jsonify, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Menu(db.Model):
    __table_name__ = 'menu'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"'{self.name}', '{self.price}'"

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/menus')
def get_menus():
    return jsonify({'menus':menus})

@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menu', methods=['PUT'])
def update_menu():
    return

@app.route('/menu', methods=['DELETE'])
def delete_menu():
    return


if __name__ == "__main__":
    app.run(debug=True)