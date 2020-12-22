from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Create table
# conn = sqlite3.connect('menus.db')
# conn.row_factory = sqlite3.Row
# c = conn.cursor()
# c.execute('''CREATE TABLE menus(id integer, name text, price integer)''')

@app.route('/')
def hello_flask():
    return "Hello World!"

# Read
@app.route('/menus')
def get_menus():
    conn = sqlite3.connect('menus.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("select * from menus")
    menus = c.fetchall()
    result = []
    for menu in menus:
        result.append(dict(menu))
    return jsonify(result)

# Create
@app.route('/menu', methods=['POST'])
def create_menu():
    # 전달받은 자료를 menus에 추가
    conn = sqlite3.connect('menus.db')
    c = conn.cursor()
    request_data = request.get_json()
    c.execute("select MAX(id) from menus")
    id = c.fetchone()
    try:
        id = tuple(id)[0] + 1
    except:
        id = 1
    name = request_data['name']
    price = request_data['price']

    c.execute("insert into menus values (?, ?, ?)", (id, name, price))
    conn.commit()
    return jsonify({"id" : id, "name" : name, "price" : price})

# Update
@app.route('/menu/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    name = request_data['name']
    price = request_data['price']
    conn = sqlite3.connect('menus.db')
    c = conn.cursor()
    c.execute("update menus set name=? where id=?", (name, id))
    c.execute("update menus set price=? where id=?", (price, id))
    conn.commit()
    return jsonify({"id" : id, "name" : name, "price" : price})

# Delete
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    conn = sqlite3.connect('menus.db')
    c = conn.cursor()
    c.execute("delete from menus where id=?", (id,))
    conn.commit()
    return jsonify({"메뉴 삭제": id})


if __name__ == '__main__':
    app.run()