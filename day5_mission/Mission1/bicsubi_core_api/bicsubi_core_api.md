# Bicsubi API 명세서

## 1. Return github id 
    GET /whoami
### Request
**Not required.**
### Response

    {
        "name": "Gangneng"
    }

---
## 2. Return string 
    GET /echo?string="string"
### Request
**Not required.**
### Response

    {
        "string": "string"
    }

---
## **CRUD Weapon list**

## 3. Read Weapon list
    GET /weapon
### Request
**Not required.**
### Response

    {
        "weapons": [
            {
                "name": "shield",
                "stock": 5
            }
        ]
    }

---
## 4. Create weapon
    POST /weapon
or

    POST /weapon?name="weapon_name"&stock="weapon_stock"

or

    POST /weapon/"weapon_name"/"weapon_stock"
### Request
**In first case,**

    {
        "name" : "weapon_name",
        "stock" : weapon_stock
    }
**The rest of the case, Not required.**
### Response

    {
        "weapons": [
            {
                "id" : 1
                "name": "weapon_name",
                "stock": weapon_stock
            },
        ]
    }
### *Exception*
**When you try to put in weapon that already exists**
### Response

    Warning!!! Already exist weapon
---
## 5. Update weapon
    PUT /weapon?name="weapon_name"

or

    PUT /weapon/"weapon_name"
### Request
    {
        "name" : "new_weapon_name",
        "stock" : new_weapon_stock
    }
or

    {
        "stock" : new_weapon_stock
    }
### Response

    {
        "weapons": [
            {
                "id" : 1
                "name": "new_weapon_name" / "weapon_name"
                "stock": new_weapon_stock
            },
        ]
    }
### *Exception*
**When you try to put in weapon that already exists**
### Response

    Warning!!! Already exist weapon
### *Exception*
**When you try to put update a weapon that is missing**
### Response

    Warning!!! Not exist weapon
