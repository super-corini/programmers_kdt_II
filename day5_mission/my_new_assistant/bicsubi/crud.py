from sqlalchemy.orm import Session

import model, schema


def get_all_weapon(db: Session):
    return db.query(model.Weapon).all()


def get_weapon_by_name(db: Session, weapon_name: str):
    db_weapon = db.query(model.Weapon).filter_by(name = weapon_name).first()
    return db_weapon


def create_weapon(db: Session, weapon: schema.Weapon):
    db_weapon = model.Weapon(name=weapon.name, stock=weapon.stock)

    db.add(db_weapon)
    db.commit()
    db.refresh(db_weapon)

    return db_weapon


def update_weapon(db: Session, weapon_name: str, mod_info: schema.ModifyWeapon):
    db_weapon = db.query(model.Weapon).filter_by(name = weapon_name).first()
    
    if mod_info.name:
        db_weapon.name = mod_info.name
    if mod_info.stock:
        db_weapon.stock = mod_info.stock

    db.add(db_weapon)
    db.commit()
    db.refresh(db_weapon)

    return db_weapon


def delete_weapon(db: Session, weapon_name: str):
    db_weapon = db.query(model.Weapon).filter_by(name = weapon_name).first()
    
    db.delete(db_weapon)
    db.commit()

    return db_weapon.name