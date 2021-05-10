from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model) :
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) :
        return "<Menu('{}', '{}', '{}')>".format(self.id, self.name, self.price)

    def to_json(self) :
        return {'id':self.id, 'name':self.name, 'price':self.price}
        
def search_by_id(id) :
    return Item.query.filter_by(id = id).first()

def search_by_name(name) :
    return Item.query.filter_by(name = name).all()

def query_all() :
    return Item.query.all()