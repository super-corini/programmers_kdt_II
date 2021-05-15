from flask import Flask, jsonify, request, abort
import pymysql

app = Flask(__name__)

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='bicsubi', charset='utf8')
curs = db.cursor()

@app.route('/whoami')
def whoami():
    return jsonify({"name":'wkdclrms123'})

@app.route('/echo')
def string():
    string = request.args.get('string')
    return jsonify({'value':f'{string}'})

# Create
@app.route('/<int:stock>', methods=['POST'])
def create(stock):
    weapon_name = request.args.get('weapon')
    sql = ''' INSERT INTO `weapon`(`name`, `stock`)
                VALUES (%s, %s)'''
    curs.execute(sql, [weapon_name, stock])
    db.commit()        
    return "CREATE COMPLETE!"

# Read
@app.route('/show')
def read():
    sql = "SELECT * FROM weapon;"
    curs.execute(sql)
    return jsonify(curs.fetchall())

# Update
@app.route('/update_weapon', methods=['PUT'])
def update():
    weapon_name = request.args.get('weapon')
    
    sql = 'SELECT name FROM weapon WHERE name=%s'
    curs.execute(sql, weapon_name)
    a = len(curs.fetchall())
    if a == 0:
        abort(404)
    new_weapon = request.get_json() # {weapon:name, stock:stock}
    sql = '''UPDATE `weapon` SET name = %s, stock = %s
            WHERE name = %s
            '''
    curs.execute(sql, [new_weapon['weapon'], new_weapon['stock'], weapon_name])
    db.commit()
    return "UPDATE COMPLETE!"

# Delete
@app.route('/delete', methods=['DELETE'])
def delete():
    weapon_name = request.args.get('weapon')
    sql = 'SELECT name FROM weapon WHERE name=%s'
    curs.execute(sql, weapon_name)
    a = len(curs.fetchall())
    if a == 0:
        abort(404)

    sql = 'DELETE FROM `weapon` WHERE name = %s'
    curs.execute(sql, weapon_name)
    db.commit()
    return "DELETE COMPLETE!"

if __name__ == '__main__':
    app.run(debug=True, port=80)