from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(32), unique=True)
    stock = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'stock': self.stock
        }