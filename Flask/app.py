from flask import Flask, render_template, Response, url_for, request, redirect
import mysql.connector

app = Flask(__name__)

''' DB 연동 '''

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = "0000",
    database = "menu"
)
@app.route("/")
def home():

    return render_template("index.html")

@app.route("/menu")
def menu():
    my_cursor = mydb.cursor()
    my_cursor.execute("select * from menutbl;")
    data = my_cursor.fetchall()
    menus = []
    for i in data:
        menus.append({'id':i[0],'name':i[1],'price':i[2]})

    return render_template("index.html", menulist=menus)

@app.route("/menu",methods=['POST'])
def newmenu():
    my_cursor = mydb.cursor()
    sql = "insert into menutbl (dbname, dbprice) values (%s, %s);"
    my_cursor.execute(sql, (request.form['lname'],request.form['lprice']))
    mydb.commit()
    return redirect(url_for("menu"))

@app.route("/update",methods=['POST'])
def updatemenu():
    my_cursor = mydb.cursor()
    sql = "update menutbl set dbname = %s , dbprice = %s where id = %s ;"
    my_cursor.execute(sql,(request.form['lname'],request.form['lprice'],request.form['lid']))
    mydb.commit()
    return redirect(url_for("menu"))

@app.route("/delet",methods=['POST'])
def delmenu():
    my_cursor = mydb.cursor()
    sql = "DELETE FROM menutbl WHERE id = %s"
    adr = (request.form['lid'], )
    my_cursor.execute(sql,adr)
    mydb.commit()
    numset()
    return redirect(url_for("menu"))


def numset():
    my_cursor = mydb.cursor()
    sql = "ALTER TABLE menutbl AUTO_INCREMENT=1;"
    my_cursor.execute(sql)
    sql = "SET @count=0;"
    my_cursor.execute(sql)
    sql = "UPDATE menutbl SET id=@count:=@count+1;"
    my_cursor.execute(sql)
    mydb.commit()

if __name__ == "__main__":
    app.run()


'''  bd 없을때
menus = [{"id":1, "name":"caffee" ,"price":10000},
    {"id":2, "name":"latte" ,"price":12000},
    {"id":3, "name":"banana" ,"price":10000}
]


menus 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():

    return render_template("index.html", menulist=menus)

@app.route("/menu",methods=['POST'])
def newmenu():
    new = {
        "id":request.form['lid'],
        "name":request.form['lname'],
        "price" : request.form['lprice']
    }
    
    menus.append(new)
    return redirect(url_for("menu"))

@app.route("/update",methods=['POST'])
def updatemenu():
    new = {
        "id":request.form['lid'],
        "name":request.form['lname'],
        "price" : request.form['lprice']
    }
    menus[int(request.form['lid'])-1] = new

    return redirect(url_for("menu"))

@app.route("/delet",methods=['POST'])
def delmenu():
    del menus[int(request.form['lid'])-1]
    numset()
    return redirect(url_for("menu"))

def numset():
    for num, i in enumerate(menus):
        i['id'] = num+1
    

if __name__ == "__main__":
    app.run()
'''
