from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Weapons(db.Model):
    __tablename__ = 'weapons'

    name = db.Column(db.String(50), primary_key=True)
    stock = db.Column(db.Integer)

    def get_weapon():
        return [{'name': weapon.name, 'stock': weapon.stock} for weapon in Weapons.query.all()]

    def add_weapon(name, stock):
        weapon = db.session.query(Weapons).filter(Weapons.name == name).first()
        if weapon is not None:
            return '같은 무기를 가지고 있습니다. 다른 무기를 추가해주세요'
        weapon = Weapons(name=name, stock=stock)
        db.session.add(weapon)
        db.session.commit()
        return {"name": name, "stock": stock}

    def update_weapon(name, stock):
        weapon = db.session.query(Weapons).filter(Weapons.name == name).first()
        if weapon is None:
            return "찾는 무기가 없습니다. 추가해 주시길 바랍니다."
        weapon.name, weapon.stock = name, stock
        db.session.commit()
        return {"name": name, "stock": stock}

    def delete_weapon(name):
        weapon = db.session.query(Weapons).filter(Weapons.name == name['name']).first()
        if weapon is None:
            return "찾는 무기가 없습니다."
        del_weapon_name = weapon.name
        del_weapon_stock = weapon.stock
        db.session.delete(weapon)
        db.session.commit()
        return {"삭제된 무기": del_weapon_name, "수량": del_weapon_stock}
