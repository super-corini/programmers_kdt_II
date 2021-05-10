from flask import Flask,jsonify,request
import sqlite3

conn=sqlite3.connect('test.db')

c=conn.cursor()

c.execute("CREATE TABLE cafe(id integer,name varchar(50),price integer)")

c.execute("INSERT INTO cafe VALUES(1,'Espresso', 3000)")

c.execute("INSERT INTO cafe VALUES(2,'ICE Espresso', 4000)")

c.execute("INSERT INTO cafe VALUES(3,'Latte', 3500)")


conn.commit()
app=Flask(__name__)



@app.route('/')
def hello_flask():

    return "Hello World"

@app.route('/menus',methods=['GET'])
def get_menus():
    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute('SELECT * FROM cafe')
    a = c.fetchall()
    con.commit()
    con.close()
    return jsonify({"menus":a})

@app.route('/menus', methods=['POST'])
def create_menus():
    request_data=request.get_json()
    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute('SELECT COUNT(*) FROM cafe')
    id,name,price=c.fetchone()[0]+1,request_data['name'],request_data['price']
    c.execute('INSERT INTO cafe (id,name,price) VALUES (?,?,?)',(id,name,price))
    c.execute('SELECT * FROM cafe')
    m=c.fetchall()
    con.commit()
    con.close()

    return jsonify({"menus":m})

@app.route('/menus/<int:id>',methods=['PUT'])
def update_menus(id):
    request_data=request.get_json()
    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute('UPDATE cafe SET name=?,price=? WHERE id=?',(request_data['name'],request_data['price'],id))
    c.execute('SELECT * FROM cafe')
    m=c.fetchall()
    con.commit()
    con.close()
    return jsonify({"menus":m})
@app.route('/menus/<int:id>',methods=['DELETE'])
def delete_menus(id):
    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute("DELETE FROM cafe WHERE id= :ID",{"ID":id})
    c.execute('SELECT * FROM cafe')
    m=c.fetchall()
    con.commit()
    con.close()
    return jsonify({"menus":m})
if __name__=='__main__':
    app.run()