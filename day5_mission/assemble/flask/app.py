# Mission 1. My New Assistant
'''
제출할 파일 bisubi_core_api.md , API 구축에 사용되는 파일들
다음의 명세에 맞게 API를 작성합니다

GET /whoami
여러분의 github id 를 반환합니다

GET / echo?string="string"
Query String : string <- 이거 아님
***수정*** 받은값중 string 안에 string 값을 반환
string 을 반환합니다

다음의 요구사항에 맞게 API를 설계하고 작성합니다
-빅수비는 자원 weapon을 가집니다. 이 weapon 은 이름(name: str)과 수랑(stock: int)을 가지며 각각에 대하여 Create, Read, Update, Delete를 진행할 수 있습니다.
 Create :새로운 weapon 추가
 Read : 현재 존재하는 weapon을 확인
 Update : 현재 존재하는 weapon의 특정 속성 name, stock 수정
 Delete : 현재 존재하는 특정 weapon을 삭제
-작성한 API에 대한 명세 (API Docs)를 bicsubi_core_api.md에 작성하여 제출합니다.
-모든 API는 작성자가 설계한대로 원활하게 동작되어야 합니다
'''

# Mission 1. Extra Mission 
'''
-제출할 파일 :bicsubi_extra_api.md ,API 구축에 사용되는 파일들
-다음의 명세서에 맞게 API를 설계하고 작성합니다
    현재 위치의 위도와 경도 값을 이용해 현재 위치의 날씨 (온도, 바람세기 등)을 알 수 있는 API
    현재 위치의 위도와 경도 값을 이용해 현재 위치에서 가장 가까운 버스정류장의 도착정보를 알수 있는 API
-Swagger를 이용해 API Docs를 만듭니다.
-작성한 API에 대한 명세(API Docs)를 bicsubi_extra_api.md에 작성하여 제출합니다.
-모든 API 작성자가 설계한대로 원활하게 동작 되어야 합니다
-이 과제는 필수 과제 이후에 진행되어야합니다
'''


from flask import Flask, render_template, Response, url_for, request, redirect

app = Flask(__name__)


gitid =  "liebespaar93"
heroname = ""
weapon = [{'id':1,'name':'초급자 단검', 'stock': 1 }]

@app.route("/")
def home():
    print(request)
    return render_template("index.html")

@app.route("/whoami", methods=['GET'])
def whoami():
    return render_template("index.html", name_h = gitid)

@app.route("/echo")
def echo():
    heroname = request.args.get('heroname')    
    return render_template("login.html", heroname_h = heroname, weaponlist_h= weapon)

## weapon 만들기

@app.route("/weaponlist/view")
def weaponlist():
    return render_template("login.html",weaponlist_h = weapon)

@app.route("/weaponlist/create", methods=['POST'])
def weaponcreate():
    new = {
        "id":request.form['lid'],
        "name":request.form['lname'],
        "stock" : request.form['lstock']
    }
    weapon.append(new)
    return render_template("login.html",weaponlist_h =weapon)

@app.route("/weaponlist/update", methods=['POST'])
def weaponupdate():
    new = {
        "id":request.form['lid'],
        "name":request.form['lname'],
        "stock" : request.form['lstock']
    }
    weapon[int(request.form['lid'])-1] = new

    return render_template("login.html",weaponlist_h =weapon)

@app.route("/weaponlist/delete", methods=['POST'])
def weapondelete():
    del weapon[int(request.form['lid'])-1]
    numset()
    return render_template("login.html",weaponlist_h =weapon)

def numset():
    for num, i in enumerate(weapon):
        i['id'] = num+1





if __name__ == "__main__":
    app.run(debug=True)