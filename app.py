from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

#db_init
table_name = "menus"
conn = sqlite3.connect("test.db",check_same_thread=False)
cur = conn.cursor()
"""
menus = [
    {"id":1,"name":"Espresso","price":3800},
    {"id":2,"name":"Americano","price":4100},
    {"id":3,"name":"CafeLatte","price":4600}
]
cur.execute("CREATE TABLE "+ table_name +" (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100) NOT NULL, price INTEGER NOT NULL)")
for item in menus:
    insert(cur,conn,item['name'],item['price'])
"""

def insert(name, price):
    cur.execute(
        "insert into " + table_name +" (name, price) values (" +  
        "'" + name +  "'," +
        str(price) + ")")
    conn.commit()

def select_all():
    cur.execute("select * from " + table_name)
    rows = cur.fetchall()
    return rows

def delete(id):
    cur.execute(
        "delete from " + table_name + " where id = " + str(id)
    )
    conn.commit()

def update(id,name,price):
    cur.execute(
        "update " + table_name + " set name = '"+name+"', price = "+str(price)+" where id = "+str(id) 
    )
    conn.commit()

@app.route('/menus') 
def get_menus():
    return jsonify(select_all())

@app.route('/menus', methods=['POST'])
def create_menus():
    request_data = request.get_json()
    insert(request_data['name'],request_data['price'])
    return jsonify(select_all())

@app.route('/menus/<int:id>',methods=['PUT'])
def update_menus(id):
    request_data = request.get_json()
    update(id,request_data['name'],request_data['price']) 
    return jsonify(select_all())

@app.route('/menus/<int:id>',methods=['DELETE'])
def delete_menus(id):
    delete(id)
    return jsonify(select_all())

@app.route('/')
def hello_flask():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
