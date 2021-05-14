from flask import Flask, jsonify, request
import sqlite3
app = Flask(__name__)


#####DB 생성 sqlite####
try:
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("CREATE TABLE weapons (id int, name varchar(50), stock int)")
    conn.commit()
    conn.close()
except:
    pass


@app.route('/')
def index():
    return 'Mission1'

@app.route('/whoami')
def whoami():
    return jsonify({'name': 'jung9156'})
    
@app.route('/echo/<echo_message>')
def echo(echo_message):
    return jsonify({'value': echo_message})
    
@app.route('/weapon/create', methods=['POST'])
def create_weapon():
    weapon_info = request.get_json()
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    weapon_num2 = list(c.execute('SELECT id FROM weapons'))
    if len(weapon_num2) == 0:
        weapon_num = 0
    else:
        weapon_num = int(max(weapon_num2)[0]) + 1

    c.execute('INSERT INTO weapons VALUES (?, ?, ?)', (weapon_num, weapon_info['name'], weapon_info['stock']))
    conn.commit()
    conn.close()
    return jsonify({'id': weapon_num, 'name': weapon_info['name'], 'stock': weapon_info['stock']})

@app.route('/weapon/read')
def read_weapon():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    weapons = list(c.execute('SELECT * FROM weapons'))
    weapon_list = {}
    conn.commit()
    conn.close()
    #####질문이 있습니다! 여기서 json형식으로 매번 만들어서 weapon리스트를 반환하는데 sqlite에서 바로 json형식으로 보내는건 어떻게 해야 할까요??##
    for weapon in weapons:
        wid, wname, wstock = weapon
        weapon_list[wid] = {'id': wid, 'name': wname, 'stock': wstock}
    return jsonify(weapon_list)

@app.route('/weapon/update/<int:weapon_id>', methods=['POST'])
def update_weapon(weapon_id):
    weapon_info = request.get_json()
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute('UPDATE weapons SET name=(?), stock=(?) WHERE id == (?)', (weapon_info['name'], weapon_info['stock'], weapon_id))
    conn.commit()
    conn.close()
    return jsonify({'id': weapon_id, 'name': weapon_info['name'], 'stock': weapon_info['stock']})

@app.route('/weapon/delete/<int:weapon_id>', methods=['POST'])
def delete_weapon(weapon_id):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("DELETE FROM weapons WHERE id == {}".format(weapon_id))
    newweapon_list = list(c.execute('SELECT * FROM weapons'))
    conn.commit()
    conn.close()
    weapon_list = {}
    for weapon in newweapon_list:
        wid, wname, wstock = weapon
        weapon_list[wid] = {'id': wid, 'name': wname, 'stock': wstock}
    return weapon_list

###extra 나중에 하기!

if __name__ == '__main__':
    app.run()