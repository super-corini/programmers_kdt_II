from flask import Flask, jsonify, request
from mysql_mgr import *

app = Flask(__name__)

# SQL 결과를 dictionary로 만들어주기 위한 메소드
def to_dict(values):
    res = {"id": values.id,
           "name": values.name,
           "price" : values.price
           }

    return res


@app.route('/')
def hello_code():
    return 'Hello World!'

# GET /menu
@app.route('/menu') 
def get_menus(): 
    # menu DB의 모든 데이터 select
    result = mysql_select_all()         
    res_list = []
            
    for item in result:     
        # select 결과를 dictionary로 만들어 append
        res_list.append(to_dict(item))  
    
    # 결과 JSON 형태로 리턴
    return jsonify({"menus": res_list}) 
    

# POST /menu
@app.route('/menu', methods=['POST']) 
def create_menu():
    request_data = request.get_json()  
    new_menu = {
        "name": request_data['name'],
        "price": request_data['price']
    }
    
    # 요청한 데이터로 insert 수행
    mysql_insert(new_menu['name'], new_menu['price'])
    
    return jsonify(new_menu)


# PUT /menu/<int:id>
@app.route('/menu/<int:menu_id>', methods=['PUT']) 
def update_menu(menu_id):
    request_data = request.get_json()
    modified_menu = {
        "id": menu_id,
        "name": request_data['name'],
        "price": request_data['price']
    }
    
    # 요청한 데이터로 update 수행
    mysql_update(menu_id, modified_menu['name'], modified_menu['price'])
        
    return jsonify(modified_menu)


# DELETE /menu/<int:id>
@app.route('/menu/<int:menu_id>', methods=['DELETE']) 
def delete_menu(menu_id):
    # 삭제할 데이터 리턴해주기 위해 먼저 select 수행    
    result = mysql_select(menu_id)
    delete_menu = []
    for item in result:
        delete_menu.append(to_dict(item))
    
    # 요청한 id delete 수행
    mysql_delete(menu_id)
    
    return jsonify({"deleted_menu": delete_menu})
    
    
if __name__ == '__main__':
    app.run()