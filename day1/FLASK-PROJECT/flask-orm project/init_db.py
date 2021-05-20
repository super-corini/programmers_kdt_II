from app import db, Menus


db.create_all()
m1 = Menus(name = "Espresso", price = 3800)
m2 = Menus(name = "Americano", price = 4100)
m3 = Menus(name = "CafeLatte", price = 4600)
db.session.add(m1)
db.session.add(m2)
db.session.add(m3)
db.session.commit()