# ref: https://medium.com/analytics-vidhya/building-rest-apis-using-flask-restplus-sqlalchemy-marshmallow-cff76b202bfb

from db import db
from typing import List


class WeaponModel(db.Model):
    __tablename__ = "weapons"

    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), primary_key=True)
    stock = db.Column(db.Integer, nullable=False)

    # store_id =db.Column(db.Integer,db.ForeignKey('stores.id'),nullable=False)
    # store = db.relationship("StoreModel",)

    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
        # self.store_id = store_id

    def __repr__(self):
        return 'WeaponModel(name=%s, stock=%s)' % (self.name, self.stock)

    def json(self):
        return {'name': self.name, 'stock': self.stock}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    # @classmethod
    # def find_by_id(cls, _id) -> "WeaponModel":
    #     return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()