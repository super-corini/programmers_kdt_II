from flask import Flask, jsonify, request
import sqlite3
import json
app = Flask(__name__)

menus = [
    {'id':1, 'name':'Espresso', 'price': 3800},
    {'id':2, 'name':'Americano', 'price': 2800},
    {'id':3, 'name':'CafeLatte', 'price': 4400},
]
try:
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("CREATE TABLE menus (id int, name varchar(50), price int)")
    for me in menus:
        m1, m2, m3 = me.values()
        c.execute("INSERT INTO menus VALUES(?, ?, ?)", (m1, m2, m3))
    conn.commit()
    conn.close()
except:
    pass



@app.route('/')
def hello_flask():
    return "Hello World!"

#GET
@app.route('/menus')
def get_menut():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    menus = list(c.execute('SELECT * FROM menus'))
    conn.commit()
    conn.close()
    menuboard = {'menus': []}
    for m in menus:
        mid, mname, mprice = m
        menuboard['menus'].append({'id': mid, 'name': mname, 'price': mprice})
    return json.dumps(menuboard)

#POST
@app.route('/menus', methods=['POST'])
def create_menu():# request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    request_data = request.get_json() # {'name':'...', 'price': ...},
    nc = list(c.execute('SELECT id FROM menus'))
    new_id = int(max(nc)[0]) + 1
    c.execute("INSERT INTO menus VALUES (?, ?, ?)", (new_id, request_data['name'], request_data['price']))
    conn.commit()
    conn.close()
    return jsonify({'id': new_id, 'name': request_data['name'], 'price': request_data['price']})

# PUT
@app.route('/menus/<int:menu_id>', methods=['PUT'])
def change_menu(menu_id):
    request_data = request.get_json()
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    updatemenu = c.execute("UPDATE menus SET name=(?), price=(?) WHERE id == (?)", (request_data['name'], request_data['price'], menu_id))
    conn.commit()
    conn.close()
    return jsonify({'id': menu_id, 'name': request_data['name'], 'price': request_data['price']})

#DELETE
@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def del_menu(menu_id):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("DELETE FROM menus WHERE id == {}".format(menu_id))
    deletedmenus = list(c.execute('SELECT * FROM menus'))
    menuboard = {'menus': []}
    for m in deletedmenus:
        mid, mname, mprice = m
        menuboard['menus'].append({'id': mid, 'name': mname, 'price': mprice})

    conn.commit()
    conn.close()
    return json.dumps(menuboard)

if __name__ == '__main__':
    app.run()





    ################보너스 2 이전 코드#####################
# from flask import Flask, jsonify, request


# app = Flask(__name__)


# menus = [
#     {'id':1, 'name':'Espresso', 'price': 3800},
#     {'id':2, 'name':'Americano', 'price': 2800},
#     {'id':3, 'name':'CafeLatte', 'price': 4400},
# ]


# @app.route('/')
# def hello_flask():
#     return "Hello World!"

# #GET
# @app.route('/menus')
# def get_menut():
#     return ({'menus': menus})

# #POST
# @app.route('/menus', methods=['POST'])
# def create_menu():# request가 JSON이라고 가정
#     # 전달받은 자료를 menus 자원에 추가
#     request_data = request.get_json() # {'name':'...', 'price': ...},
#     new_menu = {
#        'id': menus[-1]['id'] + 1,
#        'name': request_data['name'],
#         'price': request_data['price'],
#     }
#     menus.append(new_menu)
#     return jsonify(new_menu)

# #PUT
# @app.route('/menus/<int:menu_id>', methods=['PUT'])
# def change_menu(menu_id):
#     request_data = request.get_json()
#     for menu in menus:
#         if menu['id'] == menu_id:
#             menu['name'] = request_data['name']
#             menu['price'] = request_data['price']
#             return jsonify(menu)

# #DELETE
# @app.route('/menus/<int:menu_id>', methods=['DELETE'])
# def del_menu(menu_id):
#     for menu in menus:
#         if menu['id'] == menu_id:
#             menus.remove(menu)
#             return jsonify(menus)


# if __name__ == '__main__':
#     app.run()