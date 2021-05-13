from flask import Flask, jsonify, request
import os
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('weapon.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS weapon(name TEXT, amount INTEGER)')
#c.execute(isStr, ("Espresso", 3800))
#c.execute(isStr, ("Americano", 4100))
#c.execute(isStr, ("CafeLatte", 4600))
conn.commit()
	
c.close()
conn.close()

@app.route('/')
def hello_flask():
	return "Hello World!"

@app.route('/whoami')
def get_name():
	git_name = {
		"name" : "fantasworm"
	}
	return jsonify(git_name)

@app.route('/echo/')
def print_string():
	str_json = {
		"value" : request.args.get('string')
	}
	return jsonify(str_json)

# GET /weapons : 자료를 가지고 온다.
@app.route('/weapon')
def get_weapons():
	conn = sqlite3.connect('weapon.db')
	c = conn.cursor()
	c.execute('SELECT ROWID, name, amount FROM weapon')
	weapons = c.fetchall()
	c.close()
	conn.close()
	for i in range(len(weapons)):
		weapons[i] = {"id":weapons[i][0], "name":weapons[i][1], "amount":weapons[i][2]}
	return jsonify({"weapons": weapons})

# POST /weapons : 자료를 자원에 추가한다.
@app.route('/weapon', methods=['POST'])
def create_weapon():
	conn = sqlite3.connect('weapon.db')
	c = conn.cursor()
	#전달받은 자료를 weapons 자원에 추가
	request_data = request.get_json() # {"name" : ..., "amount" : ...}
	c.execute('INSERT INTO weapon (name, amount) VALUES (?, ?)', (request_data['name'], request_data['amount']))
	conn.commit()
	c.execute('SELECT ROWID, name, amount FROM weapon WHERE ROWID = LAST_INSERT_ROWID()')
	getinput = c.fetchone()
	new_weapon = {
		"id" : getinput[0],
		"name" : getinput[1],
		"amount" : getinput[2]
	}
	c.close()
	conn.close()
	return jsonify(new_weapon)

# PUT /weapon/<int:id> : id에 해당하는 데이터 갱신, 내용은 Body에 json으로 전달
@app.route('/weapon/<int:id>', methods=['PUT'])
def renew_weapon(id):
	conn = sqlite3.connect('weapon.db')
	c = conn.cursor()
	#전달받은 자료를 weapons 자원에 갱신
	request_data = request.get_json()
	c.execute('UPDATE weapon SET name = ?, amount = ? WHERE ROWID = ?', (request_data['name'], request_data['amount'], id))
	conn.commit()
	c.close()
	conn.close()
	renew_weapon = {
		"id" : id,
		"name" : request_data['name'],
		"amount" : request_data['amount']
	}
	return jsonify(renew_weapon)

# DELETE /weapon/<int:id> : id에 해당하는 데이터 삭제
@app.route('/weapon/<int:id>', methods=['DELETE'])
def delete_weapon(id):
	conn = sqlite3.connect('weapon.db')
	c = conn.cursor()
	c.execute('SELECT ROWID, name, amount FROM weapon WHERE ROWID = ?', (id,))
	getdel = c.fetchone()
	c.execute('DELETE FROM weapon WHERE ROWID =?', (id,))
	conn.commit()
	conn.execute('VACUUM')
	c.close()
	conn.close()
	del_weapon = {
		"id" : getdel[0],
		"name" : getdel[1],
		"amount" : getdel[2]
	}
	return jsonify(del_weapon)

if __name__ == '__main__':
	app.run()