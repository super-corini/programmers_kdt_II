from flask import url_for, Flask, jsonify, request, render_template, redirect, Response
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#db.create_all()
class Menu(db.Model):
    __table_name__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"'{self.name}', '{self.price}'"


@app.route('/', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        name = request.form['name']
        price = int(request.form['price'])
        menu = Menu(name=name, price=price)
        db.session.add(menu)
        db.session.commit()
        menus = Menu.query.all()
        return redirect(url_for("menu", menus=menus))

    else:
        menus = Menu.query.all()
        return render_template("index.html", menus=menus)

@app.route('/update', methods=['PUT'])
def update_menu():
    id = request.form['id']
    name = request.form['name']
    price = request.form['price']
    menu = Menu.query.filter_by(id=id).first()
    menu.name = name
    menu.price = price
    db.session.commit()
    return redirect('/')


@app.route('/delete', methods=['DELETE'])
def delete_menu():
    id = request.form['id']
    menu = Menu.query.filter_by(id=id).first()
    db.session.delete(menu)
    db.session.commit()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)