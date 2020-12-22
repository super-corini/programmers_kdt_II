from flask import Flask, jsonify, request
import pymysql

db = pymysql.connect(host="localhost", port = 3306, user="root", passwd = "gksrnr12", db = 'coffee_menus', charset="utf8")

cur = db.cursor()

app = Flask(__name__)


# sql = """INSERT INTO menus VALUES(1, 'Espresso', 3000), (2, 'Americano', 4000), (3, 'CafeLatte', 5000)"""
# cur.execute(sql)
# db.commit()
sql = """SELECT * FROM menus"""
cur.execute(sql)
m = cur.fetchall()
menus = {}
for item in m:
    menus[item[0]] = {
        "name" : item[1],
        "price" : item[2]
    }


@app.route('/')
def hello_flask():
    return "Hello World"

#get /menus
@app.route('/menus')
def get_menus():
    return jsonify({'menus' : menus})

#post /menus
@app.route('/menus', methods=['POST'])
def create_menus():
    request_data = request.get_json()
    size = len(menus)
    menus_key = list(menus.keys())
    id = menus_key[size - 1] + 1
    name = request_data['name']
    price = request_data['price']
    menus[id] = {
        "name" : name,
        "price" : price
    }
    sql = """INSERT INTO menus VALUES('%d', '%s', '%d')""" % (id, name, price)
    cur.execute(sql)
    db.commit()

    return jsonify(menus[id])

#put
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menus(id):
    request_data = request.get_json()
    try:
        name = request_data['name']
        price = request_data['price']
        menus[id] = {'name' : name, 'price' : price}
        sql = """UPDATE menus SET name = '%s', price = '%d' WHERE id = '%d'""" % (name, price, id)
        cur.execute(sql)
        db.commit()
    except:
        return "ID is wrong"
    return jsonify(menus[id])


@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menus(id):
    try:
        del menus[id]
        sql = """DELETE FROM menus WHERE id = '%d'""" % (id)
        cur.execute(sql)
        db.commit()
    except:
        return "ID is wrong"
    return jsonify({'menus' : menus})

if __name__ == '__main__':
    app.run()
