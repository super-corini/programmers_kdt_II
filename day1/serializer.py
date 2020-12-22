from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from models import (
    Menu
)

class MenuSchema(ModelSchema):
    class Meta:
        model = Menu
