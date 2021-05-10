from flask import Flask, render_template, Response, url_for, request, redirect

app = Flask(__name__)

menus = [{"id":1, "name":"caffee" ,"price":10000},
    {"id":2, "name":"latte" ,"price":12000},
    {"id":3, "name":"banana" ,"price":10000}
]
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
