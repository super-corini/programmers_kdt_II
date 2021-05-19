from flask import Flask, jsonify, request, current_app
from sqlalchemy import create_engine, text
import mysql.connector


app = Flask(__name__)

########################################
##############Core Mission##############
########################################

@app.route('/') 
def hello_flask():
    return "[인공지능-2기 최기웅]"


#GET /whoami
@app.route('/whoami',methods=['GET'])
def get_githubid():
    my_id = {'name' : "Kiwoong96"}
    return jsonify(my_id)

#GET /echo?string="string"
@app.route('/echo', methods=['GET']) 
def echo():
    request_data = request.args.get("string")
    my_value = {'value' : request_data} 
    return jsonify(my_value)


#Create : 새로운 weapon 을 추가
@app.route('/weapon_create', methods=['POST']) 
def create_weapons():
    request_data = request.get_json()
    new_weapon = (request_data['name'],int(request_data['stock']))
    new_weapon_dict = {'name' : new_weapon[0],
                        'stock' : new_weapon[1]}
    conn = mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='menu',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    """
    Query = ("SELECT * FROM weapons WHERE name = %s")
    cursor.execute(Query,request_data['name'])

    if cursor:
        return "Already Exist"
    """
    Query = "INSERT INTO weapons(name, stock) VALUES(%s,%s)"
    cursor.execute(Query, new_weapon)
    conn.commit()
    cursor.close() 
    conn.close()
    return jsonify(new_weapon_dict)

#Read : 현재 존재하는 weapon 을 확인
@app.route('/weapon_read', methods=['GET']) 
def read_weapons():
    DB_weapons = []

    conn = mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='menu',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    Query = ("SELECT * FROM weapons")
    cursor.execute(Query)
    for (id, name, stock) in cursor:
        DB_weapons.append({'id' : id,
                        'name' : name,
                        'stock' : stock})
    cursor.close() 
    conn.close()
    return jsonify(DB_weapons)

#Update : 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경
@app.route('/weapon_update', methods=['POST']) 
def update_weapons(): 
    request_data = request.get_json() 
    update_weapon = (request_data['name'],int(request_data['stock']),request_data['name'])
    update_weapon_dict = {'name' : update_weapon[0],
                        'stock' : update_weapon[1]}

    conn = mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='menu',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    Query = "UPDATE weapons SET name = %s, stock = %s WHERE name = %s"
    cursor.execute(Query, update_weapon)
    conn.commit()
    cursor.close() 
    conn.close()
    return jsonify(update_weapon_dict)

#Delete : 현재 존재하는 특정 weapon 을 삭제
@app.route('/weapon_delete', methods=['POST'])
def delete_weapons():
    request_data = request.get_json()
    delete_weapon = (request_data['name'],)
    delete_weapon_dict = {'name' : delete_weapon[0]}
    conn = mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='menu',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    
    """
    Query = ("SELECT * FROM weapons WHERE name = %s")
    cursor.execute(Query,delete_weapon)
    
    if not cursor:
        return "NOT Exist"
    """

    
    Query = "DELETE FROM weapons WHERE name = %s"
    cursor.execute(Query, delete_weapon)
    conn.commit()
    cursor.close() 
    conn.close()

    return jsonify(delete_weapon_dict)

#space가 메인인 경우, 즉 app.py를 직접 실행한 경우
if __name__ == '__main__':
    app.run()
