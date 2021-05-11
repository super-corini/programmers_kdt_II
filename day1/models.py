'''
Bonus 1 : id 번호 변경하여 추가하기
Bonus 2 : 데이터베이스 연동하기
'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model) :
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    # Bonus 1 : id 번호 변경하여 추가하기
    # primary key 속성을 부여하여 데이터베이스 상태에 따라 자동적으로 id가 생성
    
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