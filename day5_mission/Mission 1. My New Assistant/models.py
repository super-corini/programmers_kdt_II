from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'weapon'
    
    name = db.Column(db.String(32), primary_key=True)
    stock = db.Column(db.Integer)