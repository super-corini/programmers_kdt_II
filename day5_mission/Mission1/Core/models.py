from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MissingIdException(Exception) :
    pass

class Weapon(db.Model) :
    __tablename__ = 'weapons'

    _id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, name, stock) -> None:
        self.name = name
        self.stock = stock

    def __repr__(self) -> str:
        return 'Weapon({}, {})'.format(self.name, self.stock)
    
    def to_dict(self) :
        return {'id':self._id, 'name':self.name, 'stock':self.stock}


def search_by_id(_id) :
    item = Weapon.query.filter_by(_id = _id).first()
    if item is None :
        raise MissingIdException
    return item

def search_by_name(name) :
    item = Weapon.query.filter_by(name = name).all()
    if item is None :
        raise MissingIdException
    return item

def query_all() :
    return Weapon.query.all()
