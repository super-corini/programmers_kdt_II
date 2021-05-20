from flask import Flask, jsonify, request
import pymysql

#jsonify는 python의 dict 형식을 json으로 바꿔줌
#request는 HTTP request를 다뤄주는 모듈
db = pymysql.connect(host="localhost", user="root", passwd="1234", db="flask_test", charset="utf8")
'''db = pymysql.connect(
    user='root',
    passwd='1234',
    host='127.0.0.1',
    db='flask_test',
    charset='utf8'
)'''
cur= db.cursor()
sql = "SELECT * from test"
cur.execute(sql)
next_id=len(cur.fetchall())


app=Flask(__name__) # app이란 이름을 넣어준다는 의미
"""
menus = [{"id":0, "name":"Espresso","price":3800},
         {"id":0, "name":"Americano","price":3500},
         {"id":0, "name":"CafeLatte","price":4000},]
for i in range(len(menus)):
    menus[i]["id"]=i+1
"""
#next_id=len(menus)+1

@app.route('/')  # home directory
# python decorater란 의미 # '/'를 받았을 때 밑에 있는 함수를 작동해라
def hello_flask():
    return 'Hello World!'

# GET / menus #menus라는 자료를 접근
@app.route('/menus',methods=['GET'])
def get_menus():
    #menus가 리스트 타입이라 json으로 변환할 수 없음
    sql = "SELECT * from test"
    cur.execute(sql)
    result = cur.fetchall()
    db.commit()
    return jsonify({"menus":result})

# POST / menus #자료를 자원에 추가한다.
# GET를 제외한 method들은 반드시 명시를 해줘야함
# get은 method가 생략되어 있음
@app.route('/menus',methods=['POST'])
def create_menu():
    # 전달받은 자료를 menus자원에 추가
    """
    request_data=request.get_json()# json과 dict의 경우는 변환과정을 반드시 거쳐야함.
    new_menu={
        "id": next_id,
        "name":request_data["name"],
        "price":request_data["price"],
    }
    next_id+=1
    menus.append(new_menu)
    """
    id=next_id+1

    sql = "insert into test(id,name,price) values (%s, %s, %s)"
    cur.execute(sql,(id,request_data['name'],request_data["price"]))
    sql_sel = "SELECT * from test"
    cur.execute(sql_sel)
    result = cur.fetchall()
    db.commit()
    next_id += 1
    return jsonify({"menus":result})

@app.route('/<int:id>',methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    sql = "update test set name = %s, price= %s where id = %s"
    cur.execute(sql,(request_data['name'],request_data['price']))
    sql_sel = "SELECT * from test"
    cur.execute(sql_sel)
    result = cur.fetchall()
    db.commit()
    return jsonify({"menus": result})
    """
    for menu in menus:
        if menu['id']==id:
            menu['name']=request_data["name"]
            menu['price']=request_data["price"]
            return jsonify(menu)
    """

@app.route('/<int:id>',methods=['DELETE'])
def delete_menu(id):
    sql = "DELETE FROM test WHERE id = %s;"
    cur.execute(sql,(id))
    sql_sel = "SELECT * from test"
    cur.execute(sql_sel)
    result = cur.fetchall()
    db.commit()
    return jsonify({"menus": result})
    """
    for idx, menu in enumerate(menus):
        if menu['id']==id:
            menus.pop(idx)
            return jsonify(menus)
    """


if __name__=='__main__': # app.py를 직접적으로 실행한 경우에는 app.py를 실행해라
    app.run()
