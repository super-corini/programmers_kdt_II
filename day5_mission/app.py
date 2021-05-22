from flask import Flask, jsonify, request
import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()
c.execute("DROP TABLE weapon")
c.execute("CREATE TABLE weapon(name varchar(50),stock integer)")

c.execute("INSERT INTO weapon VALUES('maximum connection',10)")
c.execute("INSERT INTO weapon VALUES('minimum connection',2)")
c.execute("INSERT INTO weapon VALUES('speaking speed',40)")
c.execute("INSERT INTO weapon VALUES('bright',100)")
c.execute("INSERT INTO weapon VALUES('battery',76)")
conn.commit()

app = Flask(__name__)

@app.route('/whoami')
def hello_flask():
    id={
        "name":"nodenode1"
    }
    return jsonify(id)

@app.route('/echo',methods=['GET'])
def get_string():

    name=request.args.get('string')

    return jsonify({"value":name})

@app.route('/create',methods=['POST'])
def create():
    request_data = request.get_json()
    print(request_data)
    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute('INSERT INTO weapon (name,stock) VALUES (?,?)',
              (request_data['name'],request_data['stock']))
    c.execute('SELECT * FROM weapon')
    m=c.fetchall()
    print(m)
    con.commit()
    con.close()
    return jsonify({"bicsubi weapon":m})

@app.route('/read',methods=['GET'])
def read():
    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute('SELECT * FROM weapon')
    m = c.fetchall()
    con.commit()
    con.close()
    return jsonify({"bicsubi weapon":m})

@app.route('/update',methods=['PUT'])
def update():
    request_data = request.get_json()
    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute('UPDATE weapon SET name=?,stock=? WHERE name=?',
              (request_data['name'], request_data['stock'],request_data['name']))
    c.execute('SELECT * FROM weapon')
    m = c.fetchall()
    con.commit()
    con.close()
    return jsonify({"bicsubi weapon": m})


@app.route('/delete',methods=['DELETE'])
def delete():
    request_data = request.get_json()
    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute("DELETE FROM weapon WHERE name= :Name", {"Name": request_data['name']})
    c.execute('SELECT * FROM weapon')
    m = c.fetchall()
    con.commit()
    con.close()
    return jsonify({"bicsubi weapon": m})


if __name__ == '__main__':
    app.run()
