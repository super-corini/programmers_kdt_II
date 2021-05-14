from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    price = db.Column(db.Integer)


    def get_menus():
        return [{"menu.id": menu.id, "menu.name": menu.name, "menu.price": menu.price} for menu in Menu.query.all()]


    def add_menu(n, p):
        i = db.session.query(db.func.count(Menu.id)).scalar()+1
        menu = Menu(id=i, name=n, price=p)
        db.session.add(menu)
        db.session.commit()
        return {"id": i, "name": n, "price": p}


    def update_menu(i, n, p):
        menu = db.session.query(Menu).filter(Menu.id == i).first()
        if menu is None:
            return "찾으시는 id의 메뉴가 없습니다."
        menu.name, menu.price = n, p
        db.session.commit()
        return {"id": i, "name": n, "price": p}


    def delete_menu(i):
        menu = db.session.query(Menu).filter(Menu.id == i).first()
        if menu is None:
            return "찾으시는 id의 메뉴가 없습니다."
        del_menu = {"id": i, "name": menu.name, "price": menu.price}

        db.session.delete(menu)
        db.session.query(Menu).filter(Menu.id > i).update({'id': Menu.id - 1})
        db.session.commit()
        return {"삭제된 menu": del_menu}