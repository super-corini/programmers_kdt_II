# Bicsubi Core API

First mission for weekly assignment.

---
## whoami

Do yo know who am I?  

### `GET /whoami`

Display who I am.

**Code** `200 Sucess`

```json
{
    "name": "string"
}
```
---
## echo

Test query string.

### `GET /echo`

Display what I wrote.

**Code** `200 Sucess`

```json
{
    "string": "string"
}
```
---
## weapon

Handle weapons.

### `POST /weapon`

Create weapon.

**Body**

```json
{
    "name": "string",
    "stock": 0
}
```

**Code** `200` Success.

```json
{
    "name": "string",
    "stock": 0
}
```

**Code** `400` Weapon name exists in db.

```json
{
    "message": "string"
}
```

### `GET /weapon`

List all weapons.

**Code** `200` Success

```json
[
    {
        "name": "string",
        "stock": 0
    }
]
```

### `PUT /weapon`

Change weapon's name and stock given by name.

**Body**

```json
{
    "name": "string",
    "stock": 0
}
```

**Query** `name` weapon name.

**Code** `200` Success.

```json
{
    "name": "string",
    "stock": 0
}
```

**Code** `404` There is no data with name.

```json
{
    "message": "string"
}
```

### `DELETE /weapon`

Delete a weapon given its name.

**Query** `name` weapon name.

**Code** `200` Success.

```json
{
    "name": "string",
    "stock": 0
}
```

**Code** `404` There is no data with name.

```json
{
    "message": "string"
}
```

### `DELETE /weapon/init`

Initialize weapon database.

**Code** `200` Success.

```json
{
    "message": "string"
}
```