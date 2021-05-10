from flask import Flask, jsonify, request, current_app
from sqlalchemy import create_engine, text

app = Flask(__name__)

app.config.from_pyfile('config.py')
database = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0)
app.database= database


@app.route('/')
def hello_flask():
    return "Hello World!"


@app.route('/menu')
def get_menus():
    total_data=app.database.execute(text("""
        SELECT *
        FROM menu
    """)).fetchall()
    menus=[]
    for id, name, price in total_data:
        menus.append({'id':id, 'name':name, 'price':price})
    return jsonify({"menus":menus})


@app.route('/menu', methods=['POST'])
def create_menu():
    request_data = request.get_json() 
    request_id = app.database.execute(text("""
        INSERT INTO menu(
            name,
            price
        ) VALUES (
            :name,
            :price
        )
    """), request_data).lastrowid		
    new_data=app.database.execute(text("""
        SELECT
            id,
            name,
            price
        FROM menu
        WHERE id =:menu_id
    """), {
        'menu_id' : request_id
    }).fetchone()
    
    new_menu = {
        'id':new_data['id'],
        'name':new_data['name'],
        'price':new_data['price']
    } if new_data else None

    return jsonify(new_menu)

@app.route('/menu/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json() 
    check_id = app.database.execute(text("""
        SELECT
            id
        FROM menu
        WHERE id =:menu_id
    """), {
        'menu_id' : id
    }).fetchone()
    if not check_id:
        return "Error! ID:{} doesn't exist".format(id)
    request_data['id']=id
    app.database.execute(text("""
        UPDATE menu
        SET
            name=:name,
            price=:price
        WHERE
            id=:id
    """), request_data)
    return 'Success'    

@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    check_id = app.database.execute(text("""
        SELECT
            id
        FROM menu
        WHERE id =:menu_id
    """), {
        'menu_id' : id
    }).fetchone()
    print(check_id)
    if not check_id:
        return "Error! ID:{} doesn't exist".format(id)
    app.database.execute(text("""
        DELETE FROM menu
        WHERE
            id=:menu_id
    """), {
        'menu_id' : id
    })
    return 'Success'
            
if __name__=='__main__':
    app.run()