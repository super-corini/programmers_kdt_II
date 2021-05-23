from flask import Flask, jsonify, request
import os
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('cafemenu.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS cafemenu(name TEXT, price REAL)')
#c.execute(isStr, ("Espresso", 3800))
#c.execute(isStr, ("Americano", 4100))
#c.execute(isStr, ("CafeLatte", 4600))
conn.commit()
	
c.close()
conn.close()

@app.route('/')
def hello_flask():
	return "Hello World!"

# GET /menus : 자료를 가지고 온다.
@app.route('/menu')
def get_menus():
	conn = sqlite3.connect('cafemenu.db')
	c = conn.cursor()
	c.execute('SELECT ROWID, name, price FROM cafemenu')
	menus = c.fetchall()
	c.close()
	conn.close()
	for i in range(len(menus)):
		menus[i] = {"id":menus[i][0], "name":menus[i][1], "price":menus[i][2]}
	return jsonify({"menus": menus})

# POST /menus : 자료를 자원에 추가한다.
@app.route('/menu', methods=['POST'])
def create_menu():
	conn = sqlite3.connect('cafemenu.db')
	c = conn.cursor()
	#전달받은 자료를 menus 자원에 추가
	request_data = request.get_json() # {"name" : ..., "price" : ...}
	c.execute('INSERT INTO cafemenu (name, price) VALUES (?, ?)', (request_data['name'], request_data['price']))
	conn.commit()
	c.execute('SELECT ROWID, name, price FROM cafemenu WHERE ROWID = LAST_INSERT_ROWID()')
	getinput = c.fetchone()
	new_menu = {
		"id" : getinput[0],
		"name" : getinput[1],
		"price" : getinput[2]
	}
	c.close()
	conn.close()
	return jsonify(new_menu)

# PUT /menu/<int:id> : id에 해당하는 데이터 갱신, 내용은 Body에 json으로 전달
@app.route('/menu/<int:id>', methods=['PUT'])
def renew_menu(id):
	conn = sqlite3.connect('cafemenu.db')
	c = conn.cursor()
	#전달받은 자료를 menus 자원에 갱신
	request_data = request.get_json()
	c.execute('UPDATE cafemenu SET name = ?, price = ? WHERE ROWID = ?', (request_data['name'], request_data['price'], id))
	conn.commit()
	c.close()
	conn.close()
	renew_menu = {
		"id" : id,
		"name" : request_data['name'],
		"price" : request_data['price']
	}
	return jsonify(renew_menu)

# DELETE /menu/<int:id> : id에 해당하는 데이터 삭제
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
	conn = sqlite3.connect('cafemenu.db')
	c = conn.cursor()
	c.execute('SELECT ROWID, name, price FROM cafemenu WHERE ROWID = ?', (id,))
	getdel = c.fetchone()
	c.execute('DELETE FROM cafemenu WHERE ROWID =?', (id,))
	conn.commit()
	conn.execute('VACUUM')
	c.close()
	conn.close()
	del_menu = {
		"id" : getdel[0],
		"name" : getdel[1],
		"price" : getdel[2]
	}
	return jsonify(del_menu)

if __name__ == '__main__':
	app.run()