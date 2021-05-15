from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.orm import Session
import crud, model, schema
from database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

MY_NAME = "mjh0528"
tags_metadata = [
    {
        "name": "whoami",
        "description": "Wondering who I am?",
    },
    {
        "name": "echo",
        "description": "Copy ninja",
    },
]


app = FastAPI(
    title="Bicsubi",
    description="I HATE HUMAN.",
    version="1.0.1",
    openapi_tags=tags_metadata
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(
    "/whoami",
    tags=["whoami"],
    response_model=schema.Developer,
    responses={
        200: {
            "description": "Return the developer's name.",
        }
    }
)
async def show_who_am_i():
    return {"name": MY_NAME}

@app.get(
    "/echo",
    tags=["echo"],
    response_model=schema.EchoItem,
    responses={
        200: {
            "description": "OK",
        }
    }
)
async def echo_string(string: str):
    return {"value" : string}


@app.get(
    "/weapon",
    tags=["weapon"],
    response_model=schema.WeaponList,
    responses={
        200: {
            "description": "OK",
        }
    },
)
async def get_weapon_list(db: Session = Depends(get_db)):
    return {"weapons": crud.get_all_weapon(db)}


@app.post(
    "/weapon",
    tags=["weapon"],
    status_code=201,
    response_model=schema.Weapon,
    responses={
        201: {
            "description": "OK",
        },
        400: {
            "description": "Weapon already in list",
        },
    },
)
async def add_weapon(weapon: schema.Weapon, db: Session = Depends(get_db)):
    if crud.get_weapon_by_name(db, weapon.name):
        raise HTTPException(status_code=400, detail="Weapon already in list")
    return crud.create_weapon(db, weapon)


@app.put(
    "/weapon/{weapon_name}",
    tags=["weapon"],
    response_model=schema.Weapon,
    responses={
        200: {
            "description": "OK",
        },
        400: {
            "description": "Weapon already in list",
        },
        404: {
            "description": "Weapon not found",
        }
    },
)
async def modify_weapon(weapon_name, mod_info: schema.ModifyWeapon, db: Session = Depends(get_db)):
    if not crud.get_weapon_by_name(db, weapon_name):
        raise HTTPException(status_code=404, detail="Weapon not found")
    if mod_info.name:
        if crud.get_weapon_by_name(db, mod_info.name):
            raise HTTPException(status_code=400, detail="Weapon already in list")
    return crud.update_weapon(db, weapon_name, mod_info)


@app.delete(
    "/weapon/{weapon_name}",
    tags=["weapon"],
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": {
                        "name": "M16"
                    }
                }
            },
        },
        404: {
            "description": "Weapon not found",
        }
    },
)
async def delete_weapon(weapon_name, db: Session = Depends(get_db)):
    if not crud.get_weapon_by_name(db, weapon_name):
        raise HTTPException(status_code=404, detail="Weapon not found")
    return {"name": crud.delete_weapon(db, weapon_name)}