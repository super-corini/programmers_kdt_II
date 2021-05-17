> day5.py 에 구현된 mission

### 1. 기본 홈 화면 구성

```python
@app.route('/')
def week4_day5():
    return "week4_day5 mission"
```



### 2. github id를 반환

```python
my_name = [
    {
        "name" : "rsh1994"
    }
]

@app.route('/whoami')
def get_who():
    return jsonify(my_name)
```



### 3. Query String

```python
@app.route('/echo')
def get_string():
    order = request.args.get('string')
    if order:
        return jsonify({"value":order})
    return jsonify({"no no"})
```

string으로 입력받은 값을 order에 저장하여 출력



# 빅수비

```python
weapon_list = []
```

- 무기들이 저장되는 리스트

  

### 1. weapon의 리스트를 조회한다.

```python
@app.route('/weapon')
def get_weapon():
    return jsonify({"weapon" : weapon_list})
```



### 2. 새로운 무기를 추가한다. (무기가 이미 있으면 추가되지않는다.)

```python
@app.route('/weapon/', methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    if request_data['name'] not in weapon_name: #weapon_name 리스트에 무기가 없으면
        new_weapon = {
            "name": request_data['name'],
            "stock": request_data['stock']
        }
        weapon_list.append(new_weapon) # wapon.list에 추가한다.
        # wepon_name은 무기의 이름만 저장된 장소
        weapon_name.append(request_data['name']) 
    return jsonify(new_weapon)
```



### 3. 입력한 무기의 이름과 갯수 정보를 변경한다.

```python
# GET /weapon/<string:name> | 무기를 조회한다.
@app.route('/weapon/<string:name>', methods=['GET']) # 
def read_weapon(name):
    for idx, w in enumerate(weapon_list): # 변경할 무기이름을 조회한다.
        if w['name'] == name:
            return jsonify(w)
    return jsonify("X")
# POST /waepon/<string:name> | 무기를 조회한다.
@app.route('/weapon/<string:name>', methods=['POST'])
def modify_weapon(name):
    request_data = request.get_json()
    for idx, w in enumerate(weapon_list): # 변경할 무기 이름과 갯수를 업데이트한다.
        if w['name'] ==name:
            w['name'] = request_data['name']
            w['stock'] = request_data['stock']
            return jsonify(w['name'])
    return jsonify("X")
```



### 4. 해당 name의 데이터를 삭제한다.

```python
@app.route('/weapon/<string:name>', methods=['DELETE'])
def delete_weapon(name):
    for idx, w in enumerate(weapon_list):
        if w['name'] == name:
            del weapon_list[idx]
            return jsonify(w)
    return jsonify("X")
```



