from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text

app = Flask(__name__)

app.config.from_pyfile('config.py')
database = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0)
app.database= database


@app.route('/')
def hello_flask():
    return "Hello World!"

@app.route('/whoami')
def whoami():
    return jsonify({"name":"taehyun-learn"})

@app.route('/echo')
def echo():
    value = request.args.get("string")
    return jsonify({"value":value})

@app.route('/weapon')
def get_weapon():
    total_data=app.database.execute(text("""
        SELECT *
        FROM weapons
    """)).fetchall()
    weapons=[]
    for id, name, stock in total_data:
        weapons.append({'id':id, 'name':name, 'stock':stock})
    return jsonify({"weapons":weapons})

@app.route('/weapon', methods=['POST'])
def create_weapon():
    name=request.args.get("name")
    check_weapon = app.database.execute(text("""
        SELECT id
        FROM weapons
        WHERE name=:name
    """), {'name':name}).fetchone()
    if check_weapon:
        app.database.execute(text("""
            UPDATE weapons
            SET
                stock=stock+1
            WHERE
                id=:id
        """), check_weapon)
    else:
        app.database.execute(text("""
            INSERT INTO weapons(
                name,
                stock
            ) VALUES (
                :name,
                :stock
            )
        """), {'name':name, 'stock':1})
    ret = app.database.execute(text("""
        SELECT id, name, stock
        FROM weapons
        WHERE name=:name
    """), {'name':name}).fetchone()
    new_weapon={
        'id':ret['id'],
        'name':ret['name'],
        'stock':ret['stock']
    }
    return jsonify(new_weapon)

@app.route('/weapon/<int:id>', methods=['PUT'])
def update_weapon(id):
    name=request.args.get("name")
    stock=request.args.get("stock")
    check_id = app.database.execute(text("""
        SELECT
            id, name
        FROM weapons
        WHERE id =:weapon_id
    """), {
        'weapon_id' : id
    }).fetchone()
    if not check_id:
        return "Error! ID:{} doesn't exist".format(id)
    check_name = app.database.execute(text("""
        SELECT
            id, name
        FROM weapons
        WHERE name =:name
    """), {
        'name' : name
    }).fetchone()
    if check_name:
        app.database.execute(text("""
            UPDATE weapons
            SET
                stock=stock+:stock
            WHERE
                name=:name
        """), {'name':name, 'stock':stock})
        app.database.execute(text("""
            DELETE FROM weapons
            WHERE
                id=:weapon_id
        """), {
            'weapon_id' : id
        })
    else:
        app.database.execute(text("""
            UPDATE weapons
            SET
                name=:name,
                stock=:stock
            WHERE
                id=:id
        """), {'id':id, 'name':name, 'stock':stock})

    return 'Success'    

@app.route('/weapon/<int:id>', methods=['DELETE'])
def delete_weapon(id):
    check_id = app.database.execute(text("""
        SELECT
            id
        FROM weapons
        WHERE id =:weapon_id
    """), {
        'weapon_id' : id
    }).fetchone()
    if not check_id:
        return "Error! ID:{} doesn't exist".format(id)
    app.database.execute(text("""
        DELETE FROM weapons
        WHERE
            id=:weapon_id
    """), {
        'weapon_id' : id
    })
    return 'Success'
            
if __name__=='__main__':
    app.run()