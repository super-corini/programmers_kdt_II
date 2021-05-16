from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Weapon(db.Model):
    __tablename__ = 'weapon'

    name = db.Column(db.String(32), primary_key=True)
    stock = db.Column(db.Integer)


    def get_weapon():
        return [{"name": weapon.name, "stock": weapon.stock} for weapon in Weapon.query.all()]


    def add_weapon(n, s):
        if db.session.query(Weapon).filter(Weapon.name == n).first() is not None:
            return '중복된 이름이 있습니다. 값을 수정하려면 update를 이용해주세요.'
        if db.session.query(db.func.count(Weapon.name)).scalar() > 100:
            return '데이터베이스의 허용량을 초과했습니다. 데이터를 삭제해주세요.'
        weapon = Weapon(name=n, stock=s)
        db.session.add(weapon)
        db.session.commit()
        return {"dblen": c, "name": n, "stock": s}


    def update_weapon(n, p):
        weapon = db.session.query(Weapon).filter(Weapon.name == n).first()
        if weapon is None:
            return "찾으시는 name의 무기가 없습니다."
        weapon.name, weapon.stock = n, p
        db.session.commit()
        return {"name": n, "stock": p}


    def delete_weapon(n):
        weapon = db.session.query(Weapon).filter(Weapon.name == n['name']).first()
        if weapon is None:
            return "찾으시는 name의 무기가 없습니다."
        del_weapon = {"name": weapon.name, "stock": weapon.stock}

        db.session.delete(weapon)
        db.session.commit()
        return {"삭제된 Weapon": del_weapon}