from sqlalchemy import Column, Integer, String
from dataclasses import dataclass
import database


@dataclass
class Menu(database.Base):
    __tablename__ = 'menus'
    id: int
    name: str
    price: int

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    price = Column(Integer, unique=False)

    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    def __repr__(self):
        return '<Menu %r>' % (self.name)
    