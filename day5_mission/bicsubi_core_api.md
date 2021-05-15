# Swagger
Swagger API docs  
<img src="images/swagger.png" width="" height="">  

Example:  
```python
url = "https://address/weapon/w1"
qs = {"market": name, "count": "1"}
rp = requests.request("GET", url, params=qs)
```  

# Weapon
```
url: http://localhost:5000/weapon/{name}  
```
## Weapon - DELETE
### Request
name: 
```
"name_to_select"
```
### Response
#### Server Response
```
code: 200
response body: 
{
  "message": "Weapon Deleted successfully"
}
``` 
#### Response
```
code: 200
description: Sucess
```

## Weapon - GET
### Request
name: 
```
"name_to_select"
```
### Response
#### Server Response
```
code: 200
response body: 
{
  "stock": 1,
  "name": "w1"
}
``` 
#### Response
```
code: 200
description: Sucess
```  

## Weapon - PUT
source code:  
```python
weapon_data = WeaponModel.find_by_name(name)
weapon_json = request.get_json();
```  

Need 2 requests : payload, param  
Process: find data by *name* and update by *payload*.  

### Request
payload: 
```
{
  "name": "text",
  "stock": 0
}
```
name: 
```
"name_to_select"
```
### Response
#### Server Response
```
code: 200
response body: 
{
  "stock": 123456,
  "name": "w123456"
}
``` 
#### Response
```
code: 200
description: Sucess
```

# Weapons
```
url: http://localhost:5000/weapons
```
## Weapons - GET
nothig to request since this fetch all the data.  
### Request
No parameters

### Response
#### Server Response
```
code: 200
response body: 
[
  {
    "stock": 123456,
    "name": "w123456"
  },
  {
    "stock": 99,
    "name": "gun"
  },
  {
    "stock": 12,
    "name": "knife"
  },
  {
    "stock": 888,
    "name": "coffee"
  }
]
``` 
#### Response
```
code: 200
description: Sucess
```


# Whoami
```
url: http://localhost:5000/whoami
```
## Whoami - GET
### Request
Nothing to request
### Server Response
{
  "name": "marquis08"
}
### Response
```
code: 200
description: Sucess
```

# Echo
```
url: http://localhost:5000/echo
```
## Echo - GET
### Request
Nothing to request
### Server Response
```
{
  "value": null
}
```
### Response
```
code: 200
description: Sucess
```


reference:  
> <https://medium.com/analytics-vidhya/building-rest-apis-using-flask-restplus-sqlalchemy-marshmallow-cff76b202bfb>