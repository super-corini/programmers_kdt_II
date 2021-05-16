from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Menus(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    price = db.Column(db.Integer)
