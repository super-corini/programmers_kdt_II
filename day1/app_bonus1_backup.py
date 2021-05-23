from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
	{"id":1, "name":"Espresso", "price":3800},
	{"id":2, "name":"Americano", "price":4100},
	{"id":3, "name":"CafeLatte", "price":4600},
]

@app.route('/')
def hello_flask():
	return "Hello World!"

# GET /menus : 자료를 가지고 온다.
@app.route('/menu')
def get_menus():
	return jsonify({"menus": menus})

# POST /menus : 자료를 자원에 추가한다.
@app.route('/menu', methods=['POST'])
def create_menu():
	#전달받은 자료를 menus 자원에 추가
	request_data = request.get_json() # {"name" : ..., "price" : ...}
	new_menu = {
		"id" : len(menus) + 1,
		"name" : request_data['name'],
		"price" : request_data['price']
	}
	menus.append(new_menu)
	return jsonify(new_menu)

# PUT /menu/<int:id> : id에 해당하는 데이터 갱신, 내용은 Body에 json으로 전달
@app.route('/menu/<int:id>', methods=['PUT'])
def renew_menu(id):
	#전달받은 자료를 menus 자원에 갱신
	request_data = request.get_json()
	renew_menu = {
		"id" : id,
		"name" : request_data['name'],
		"price" : request_data['price']
	}
	for i in range(len(menus)):
		if menus[i]["id"] == id:
			menus[i] = renew_menu
			return jsonify(renew_menu)
	return "invalid id!", id

# DELETE /menu/<int:id> : id에 해당하는 데이터 삭제
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
	delete_done = False
	for i in range(len(menus)):
		if delete_done == False:
			if menus[i]["id"] == id:
				delprint = menus[i]
				del menus[i]
				menus[i]["id"] = i + 1
				delete_done = True
		else:
			if i < len(menus):
				menus[i]["id"] = i + 1
	if delete_done == True: 
		return jsonify(delprint)
	else:
		return "invalid id!", id

if __name__ == '__main__':
	app.run()