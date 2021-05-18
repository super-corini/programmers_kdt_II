from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(32))
    price = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }