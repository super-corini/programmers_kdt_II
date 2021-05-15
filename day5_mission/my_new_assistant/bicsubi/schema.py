from pydantic import BaseModel

from typing import List, Optional


class Developer(BaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "mjh0528"
            }
        }


class EchoItem(BaseModel):
    value: str

    class Config:
        schema_extra = {
            "example": {
                "value": "string"
            }
        }


class Weapon(BaseModel):
    name: str
    stock: int

    class Config:
        orm_mode=True
        schema_extra = {
            "example": {
                "name": "M16",
                "stock": 10
            }
        }


class ModifyWeapon(BaseModel):
    name: Optional[str] = None
    stock: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "M16",
                "stock": 10
            }
        }
        

class WeaponList(BaseModel):
    weapons: List[Weapon]

    class Config:
        schema_extra = {
            "example": {
                "weapons": [
                    {
                        "name": "M16",
                        "stock": 10
                    },
                    {
                        "name": "AK-47",
                        "stock": 8
                    },
                ]
            }
        }