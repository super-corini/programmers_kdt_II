from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Weapon(db.Model) : #{
    __tablename__ = 'weapon'

    name  = db.Column(db.String(32), primary_key=True)
    stock = db.Column(db.Integer)

    def __init__(self, name, stock) : #{
        self.name = name
        self.stock = stock
    #}

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}
#}