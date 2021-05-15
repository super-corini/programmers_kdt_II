from sqlalchemy import Column, Integer, String

from database import Base


class Weapon(Base):
    __tablename__ = "weapon"

    name = Column(String(20), nullable=False, primary_key=True)
    stock = Column(Integer, nullable=False)