# REST API

If you stop running flask, it doesn't store anything unless you have a DB.  

# Flask DB Connection

## Table Create
```python
python app_db.py
```
and Exit

## Sqlite
```terminal
sqlite3 db.sqlite
```
Check tables
```terminal
.tables
```
Exit sqlite:  
Ctrl+d

## Flask Shell
Run Flask Shell on conda env or venv:  
```terminal
flask shell
```

# Display GET POST DELETE PUT by screenshot
## 1. Run flask by(app.py):  
    ```terminal
    flask run
    ```  
## 2. Open POSTMAN  
### 2-1. GET http://127.0.0.1:5000/menus  
Click Send Button  
Body Section shows a empty list.  
<img src="images/GET_empty_table.png" width="" height="">

### 2-2. POST http://127.0.0.1:5000/menus  
Fill out body part below address with raw & JSON format like this:  
```json
{
    "id":1,
    "name":"Espresso",
    "price": 3800
}
```
And then Click Send Button shows:  
<img src="images/POST1.png" width="" height="">

I posted another example for practicing delete method like this:  
```json
{
    "id": 2,
    "name": "CafeLatte Venti",
    "price": 9500
}
```

Let's GET:  
<img src="images/GET_2items.png" width="" height="">  
YES. There are two items.  

### 2-3 DELETE http://127.0.0.1:5000/menus/2
!! DELETE method access by ../menus/id  
Address should be matched.  
I would delete id=2 by using DELETE.  
```python
@app.route('/menus/<id>/',methods=['DELETE'])
def delete_user(id):
    menu = Menu.query.filter_by(id=id).first_or_404()
    db.session.delete(menu)
    db.session.commit()
    return {
        'success': 'Data deleted successfully'
    }
```
RESULT:  
<img src="images/DELETE_RESULT.png" width="" height="">  
LET'S GET:  
<img src="images/DELETE_GET.png" width="" height="">  
A venti menu deleted from the table.  

### 2-4 PUT http://127.0.0.1:5000/menus/1
Let's change id=1's name like this:  
```
{
    "name": "Water",
}
```
PUT as:  
<img src="images/PUT.png" width="" height="">  
LET'S GET:  
<img src="images/PUT_GET.png" width="" height="">  

# **DONE**  

## TODO:
### - Bad request set up (POST, DELETE, PUT)
### - PUT method needs more to be done when get data with some partial changes.  
<br>

references:  
> AWESOME REF: <
<https://betterprogramming.pub/building-restful-apis-with-flask-and-sqlalchemy-part-1-b192c5846ddd>

> flask DB connection with SQLAlchemy: <https://velog.io/@poiuyy0420/%ED%8C%8C%EC%9D%B4%EC%8D%AC-Flask-DB-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0SQLAlchemy>  

> Create table with SQLAlchemy: <https://velog.io/@ywoosang/Flask-SQLAlchemy-Create-Table>

> <https://krksap.tistory.com/1799>

> <https://wings2pc.tistory.com/entry/%EC%9B%B9-%EC%95%B1%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-Python-Flask-SQLAlchemy-ORM>
