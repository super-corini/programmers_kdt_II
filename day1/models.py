from flask_sqlalchemy import SQLAlchemy

# $ flask db init
# $ flask db migrate
# $ flask db upgrade

db = SQLAlchemy()

class Menu (db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer)

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    
