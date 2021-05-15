# Mission 1. My New Assistant
## Core Mission : 빅수비를 만들어보자!
    
빅수비의 자원 weapon의 구성요소  
- 이름(name : str)
- 수량(stock : int)
  
빅수비의 기능 : CRUD
- Create(POST) : 새로운 weapon 을 추가
- Read(GET) : 현재 존재하는 weapon 을 확인
- Update() : 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경
- Delete : 현재 존재하는 특정 weapon 을 삭제


### Create(POST) 
- new_weapon을 추가하기 위해 body에서 새로운 weapon의 속성(이름, 수량)을 작성하고, request를 통해 전달한다.
- new_weapon이 weapons에 저장되고, new weapon을 반환하여 화면에 보여준다.
<pre>
<code>
@app.route('/weapon',methods=['POST'])
def create_weapon():
    request_data = request.get_json() 
    new_weapon = {
        'name': request_data['name'],
        'stock':request_data['stock']
    }
    weapons.append(new_weapon)
    return jsonify(new_weapon)
</code>
</pre>

### Read(GET) 
- weapon을 모아둔 weapons를 반환하여 현재 존재하는 weapon들을 보여준다.
<pre>
<code>
@app.route('/weapon') 
def read_weapon():
    return jsonify({"weapons":weapons})
</code>
</pre>

### Update(PUT) 
- ?name=weapon_name -> 이는 쿼리 스트링으로 문자열을 값으로 전달할 수 있다. 
- 이 방법을 사용하여 weapon의 name값을 전달하고 name값에 해당하는 weapon을 찾아서 속성(이름, 수량)을 변경한다.
- 새로운 속성값은 body에 작성한다.
- ex) http://127.0.0.1:5000/weapon?name=weapon_name
<pre>
<code>
@app.route('/weapon',methods=['PUT'])
def update_weapons():
    name = request.args.get('name')
    request_data = request.get_json()
    for weapon in weapons:
        print(weapon['name'],name)
        if weapon['name']==name:
            weapon['name'] = request_data['name']
            weapon['stock'] = request_data['stock']
            return jsonify({"weapons":weapons})
    else:
        return 'Wrong Name'
</code>
</pre>
### Delete(DELETE) 
- PUT과 동일하게 쿼리 스트링을 사용하여 삭제하고자 하는 weapon의 이름을 전달받는다.
- for문을 통해 weapons의 weapon들을 탐색하여 전달받은 name을 가진 weapon을 찾는다.
- del을 이용하여 찾아낸 weapon을 삭제한다.
<pre>
<code>
@app.route('/weapon',methods=['DELETE']) 
def delete_weapon():
    name = request.args.get('name')
    for i, weapon in enumerate(weapons):
        if weapon['name']==name:
            del weapons[i]
            return jsonify({"weapons":weapons})
    else:
        return 'Wrong Name'
</code>
</pre>