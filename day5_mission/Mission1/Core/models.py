from sqlalchemy import Column, Integer, String
from dataclasses import dataclass
import database


@dataclass
class Weapon(database.Base):
    __tablename__ = 'weapons'
    id: int
    name: str
    stock: int

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    stock = Column(Integer, unique=False)

    def __init__(self, name=None, stock=None):
        self.name = name
        self.stock = stock

    def __repr__(self):
        return '<Weapon %r>' % (self.name)
    