from flask import Flask, jsonify, request
import pymysql

# 한글 지원 방법
import os
os.putenv('NLS_LANG', '.UTF8')

# 연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
conn = pymysql.connect(
    user='root',
    passwd='1234',
    host='127.0.0.1',
    db='FLASK',
    charset='utf8'
    )
# conn = cx_Oracle.connect('sys_dba/sys@/1234/localhost:1521/system', mode = cx_Oracle.SYSDBA)
# conn = cx_Oracle.connect('sys', '1234', 'localhost:1521/system', mode = cx_Oracle.SYSDBA)
# 'sys', '1234', 'localhost:1521/system'
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hello World!\nDB Connection...'

# GET /menu
@app.route('/menus')
def get_menus():
    sql = 'SELECT * FROM MENU'
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        return e
    print('SUCCESS')
    return jsonify(result)

# POST /menus
@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    name = request_data['name']
    price = request_data['price']

    sql = f'''
    INSERT INTO MENU(NAME, PRICE) VALUES ("{name}", {int(price)});
    '''
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql)
        # cursor.rowfactory = lambda *args: dict(zip([d[0] for d in cursor.description], args))
        result = cursor.fetchone()
        conn.commit()
    except Exception as e:
        print('FAILED')
        return e
    print('SUCCESS')
    return {'name':name, 'price':price}

# UPDATE /menus
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    name = request_data['name']
    price = request_data['price']

    sql = f'''
    UPDATE MENU
    SET NAME="{name}", PRICE={price}
    WHERE ID = {id};
    '''
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        conn.commit()
    except Exception as e:
        print('FAILED')
        return e
    print('SUCCESS')
    return {'name':name, 'price':price}

# DELETE /menus
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    sql = f'''
    DELETE FROM MENU WHERE ID = {id};
    '''
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        result = cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print('FAILED')
        return e
    print('SUCCESS')
    return jsonify(result)

if __name__ == '__main__':
    app.run()
