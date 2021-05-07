# REST API

# Implementing CoffeShop Menu API

Http Method:  
GET, POST, PUT, DELETE

POST /shoes : create new resource.
GET /shoes: After checking shoes in DB, return certain resource.

Run command:  
```flask
flask run
```

# Postman
Collection: A set of API

## GET
select GET and insert local address with /menus:  
```flask
http://127.0.0.1:5000/menus
```
and Send it.  
Then the body section shows like:  
```json
{
    "menus": [
        {
            "id": 1,
            "name": "Espresso",
            "price": 3800
        },
        {
            "id": 2,
            "name": "Americano",
            "price": 4100
        },
        {
            "id": 3,
            "name": "CaffeLatte",
            "price": 4800
        }
    ]
}
```

## POST
The same address with GET.  
But, selection body bar below address and select raw type.  
And then, type the new menu you want to post as a json format like:  
```json
{
    "name":"DolceLatte",
    "price":7000
}
```

Displayed on Body selection:  
```json
{
    "id": 4,
    "name": "DolceLatte",
    "price": 7000
}
```
Send another POST as:  
```json
{
    "name":"DolceLatte Venti",
    "price":7000
}
```
Body shows:  
```json
{
    "id": 5,
    "name": "DolceLatte Venti",
    "price": 7000
}
```

GET shows:  
```json
{
    "menus": [
        {
            "id": 1,
            "name": "Espresso",
            "price": 3800
        },
        {
            "id": 2,
            "name": "Americano",
            "price": 4100
        },
        {
            "id": 3,
            "name": "CaffeLatte",
            "price": 4800
        },
        {
            "id": 4,
            "name": "DolceLatte",
            "price": 7000
        },
        {
            "id": 5,
            "name": "DolceLatte Venti",
            "price": 7000
        }
    ]
}
```

### Works!  
### Let's Solve Bonus 2 Task.