from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Menu(db.Model):
    __tablename__ = "menu"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    price = db.Column(db.Integer)

    def __init__(self, id, name, price):
        self.id=id
        self.name=name
        self.price=price
    
    def __repr__(self):
        return "<Menu({}, '{}',{})>".format(self.id,self.name,self.price)