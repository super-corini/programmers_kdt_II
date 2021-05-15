from flask import Flask
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'weeklyMissionOne'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weapons.sqlite3'  # /// 슬러쉬 3개
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Weapons(db.Model) :
    name = db.Column(db.String(50), primary_key=True)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self,name, stock):
        self.name = name
        self.stock = stock


@app.route('/')
def hello_flask():
    # DB 초기화
    db.session.query(Weapons).delete()
    db.session.commit()
    return "hello world"

#GET /whoami
@app.route('/whoami')
def bicsubi_whoami():
    return jsonify({"name" : "hook0318"})


#GET /echo?string="string"  ->  Query String
@app.route('/echo')
def bicsubi_echo():
    qs = request.args.get('string') # flask에서 query string 가져오기 함수 request.args.get('key이름')
    return jsonify({"value" : qs})



#GET /weapon 
@app.route('/weapon')
def get_weapons():
    return jsonify([{'name':weapon.name,'stock':weapon.stock} for weapon in Weapons.query.all()])

@app.route('/weapon', methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    new_weapon = Weapons(request_data['name'], request_data['stock'])

    try :
        db.session.add(new_weapon)
        db.session.commit()
        return get_weapons()
    except:
        return "Already have"

@app.route('/weapon/<string:name>', methods=['PUT'])
def update_weapon(name):
    request_data = request.get_json()
    try :
        update_weapon = Weapons.query.filter_by(name=name).first()
        update_weapon.name = request_data['name']
        update_weapon.stock = request_data['stock']
        db.session.commit()

        return get_weapons()
    
    except :
        return "ERROR!! CAN'T FIND THAT WEAPON"

@app.route('/weapon/<string:name>', methods=['DELETE'])
def delete_weapon(name):
    try :
        delete_weapon = Weapons.query.filter_by(name=name).first()
        db.session.delete(delete_weapon)
        db.session.commit()

        return get_weapons()
    
    except :
        return "ERROR!! CAN'T FIND THAT WEAPON"


if __name__ == '__main__' :
    db.create_all()
    app.run(debug=True)