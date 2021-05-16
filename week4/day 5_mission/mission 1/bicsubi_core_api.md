# bicsubi_core_api 
-  /whoami
-  /echo
-  /weapon
    -  create
    -  read
    -  update
    -  delete



```python
# 필요한 기본 라이브러리를 불러옴
from flask import Flask, jsonify, request
```

     * Serving Flask app "__main__" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: off
    

     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    


```python
app = Flask(__name__)
# 기본적인 weapon 셋팅
weapon = [
    {"id":1, "name":"Rifle", "stock":3},
    {"id":2, "name":"Pistol", "stock":4},
    {"id":3, "name":"Bazooka", "stock":2},
]
# 현재 무기 종류의 갯수를 파악하기 위한 변수
curr_id = len(weapon)
```

## 첫화면
Hello World


```python
@app.route('/')
def hello_flask():
    return "Hello World"

```

# /whoami
github id 를 return


```python
@app.route('/whoami')
def get_myname():
    return jsonify({"name" : "lltera" })
```

# /echo


```python
@app.route('/echo')
def query_string():
    return jsonify({'value' : request.args.get('string')})
```

# /weapon
- Read : get 요청시 현재 가지고 있는 모든 무기의 종류와 남은 수량을 볼 수 있다.
- Create : 똑같은 종류의 무기가 없다면 무기 리스트에 새 무기를 추가 할 수 있다.
@app.route('/weapon/**<int:id>**', methods=['PUT']) <int:id> 이부분을 <str: var> 로 문자열로 받아보려 했는데 실패했습니다 ㅠ
- Update : 무기의 id를 입력하고 id에 해당하는 무기의 이름과 남은 수량을 변경할 수 있다.
- Delete : 무기의 id를 입력하고 그 id에 무기가 등록되어 있을 경우 해당하는 무기를 리스트에서 삭제할 수 있다.


```python
# Read Weapon
@app.route('/weapon')
def read_weapon():
    return jsonify({"weapon" : weapon})
# Create Weapon
@app.route('/weapon', methods = ['POST'])
def create_weapon():
    global curr_id
    request_data = request.get_json()
    
    for i in range(curr_id):
        if request_data['name'] == weapon[i]['name']:
            return jsonify('This weapon is already existed')
            break
    else:
        curr_id += 1
        new_weapon = {
            "id" : curr_id,
            "name" : request_data['name'],
            "stock" : request_data['stock'],
         }
        weapon.append(new_weapon)
        return jsonify(new_weapon)
# Update Weapon
@app.route('/weapon/<int:id>', methods=['PUT'])
def update_weapon(id):
    update_data = request.get_json()
    weapon[id - 1]["name"] = update_data["name"]
    weapon[id - 1]["stock"] = update_data["stock"]
    return jsonify(weapon[id - 1])

# Delete Weapon
@app.route('/weapon/<int:id>', methods=['DELETE'])
def delete_weapon(id):
    for w in weapon:
        if w['id'] == id:
            del weapon[weapon.index(w)]
            break
    else:
        return "there in no weapon"
    return jsonify(weapon)

if __name__ == "__main__":
    app.run()
```
