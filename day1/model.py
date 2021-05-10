from app import db

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Menu %r>' % self.name