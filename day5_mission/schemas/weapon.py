from ma import ma
from models.weapon import WeaponModel
# from models.item import ItemModel
# from models.store import StoreModel


class WeaponSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WeaponModel
        load_instance = True
        # load_only = ("store",)
        # include_fk= True