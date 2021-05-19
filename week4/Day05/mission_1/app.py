from flask import Flask, jsonify, request
import pymysql

db = pymysql.connect(host="localhost", port=3306, user="root", password="1q2w3e", db="kdt")
cursor = db.cursor(pymysql.cursors.DictCursor)


app = Flask(__name__)  # 이 flask의 이름을 app의 변수에 넣어준다.

@app.route('/')
def hello_flask():
    return 'weapon!'


@app.route('/whoami')
def whoami():
    return jsonify({'name':'kimdy003'})


@app.route('/echo')
def query_string():
    return jsonify({'value' : request.args.get('string')})


# Read : 현재 존재하는 `waepon`을 확인
@app.route('/weapon')
def get_weapons():
    cursor.execute("SELECT * FROM weapons")
    return jsonify(cursor.fetchall())


# CREATE : 새로운 `weapon`을 추가
@app.route('/weapon', methods=['POST'])
def create_weapon():
    request_data = request.get_json()

    sql = """
        INSERT INTO weapons 
                    (`id`, `name`, `stock`)
                VALUES 
                    ((SELECT IFNULL(MAX(id) + 1, 1) from weapons m), %s, %s)
    """
    cursor.execute(sql, (request_data['name'], request_data['stock']))
    db.commit()
    cursor.execute("SELECT * FROM weapons")
    return jsonify(cursor.fetchall())


#Update : 현재 존재하는 `weapon` 에서 특정 속성(이름, 수량)을 변경
@app.route('/weapon/<int:weapon_id>', methods=['PUT'])
def update_weapon(weapon_id):
    request_data = request.get_json()

    sql = """
        UPDATE weapons SET name=%s, stock=%s
        WHERE id=%s
    """
    cursor.execute(sql, (request_data['name'], request_data['stock'], weapon_id))
    db.commit()
    cursor.execute("SELECT * FROM weapons")
    return jsonify(cursor.fetchall())


#Delete : 현재 존재하는 특정 `weapon` 을 삭제
@app.route('/weapon/<int:weapon_id>', methods=['DELETE'])
def del_weapon(weapon_id):
    sql = '''
        DELETE FROM weapons 
        WHERE id=%s
    '''
    cursor.execute(sql, (weapon_id))
    db.commit()
    cursor.execute("SELECT * FROM weapons")
    return jsonify(cursor.fetchall())


if __name__ == '__main__':
    app.run()