# Bicsubi API

## 1. /whoami

    @app.route('/whoami', methods=['GET'])
    def  whoami():
		return  jsonify({"name" : "DongIk-Jang"})

> **github id 반환**

    {
    "name": "DongIk-Jang"
    }

## 2. /echo?string=string

    @app.route('/echo')
    def  echo():
	    echo_string = request.args.get('string', '')
	    return  jsonify({"value" : echo_string})

> **주소창에 입력한 srtring 반환**

    {
    "value": "string"
    }

## 3. /weapons/create

    @app.route('/weapons/create', methods=['POST'])
	def  create_weapon():
		request_data = request.get_json()
		new_weapon = {
			"name" : request_data['name'],
			"stock" : request_data['stock']
		}
		for  i  in  range(len(weapon)):
			if  weapon[i]['name'] == request_data['name']:
				weapon[i]['stock'] += request_data['stock']
					return  jsonify(new_weapon)
		else:
			weapon.append(new_weapon)
			return  jsonify(new_weapon)

> **이미 존재하는 name이라면 stock의 수에 입력받은 값을 더해주고 존재하지 않던 name이라면 weapon 자원에 추가하고 추가된 값 반환**
### 입력:
    {
    "name" : "Thor Hammer",
    "stock" : 1
    }
### 출력:
    {
    "name" : "Thor Hammer",
    "stock" : 1
    }

## 4. /weapons/read

    @app.route('/weapons/read')
	def  read_weapon():
		return  jsonify(weapon)

> **weapon 자원의 상태 출력**

    [
	    {
		    "name": "test weapon",
		    "stock": 1
		},
		{
			"name": "Thor Hammer",
			"stock": 1
		}
	]

## 5. /weapons/update

    @app.route('/weapons/update', methods=['PUT'])
	def  update_weapon():
		request_data = request.get_json()
		update_weapon = {
			"name" : request_data['name'],
			"stock" : request_data['stock']
		}
		for  i  in  range(len(weapon)):
			if  weapon[i]['name'] == request_data['name']:
				weapon[i] = update_weapon
		return  jsonify(update_weapon)

> **"name"과 "stock"을 json으로 입력받아서 기존 weapon 자원에 존재한다면 입력된 정보로 업데이트한 후 업데이트 내용을 반환**

### 입력:

    {
	"name" : "test weapon",
	"stock" : 2
	}
### 출력:
    {
	"name" : "test weapon",
	"stock" : 2
	}

## 6. /weapons/delete

    @app.route('/weapons/delete', methods=['DELETE'])
	def  delete_weapon():
		request_data = request.get_json()
		for  i  in  range(len(weapon)):
			if  weapon[i]['name'] == request_data['name']:
				if  weapon[i]['stock'] >= request_data['stock']:
					weapon[i]['stock'] -= request_data['stock']
					return  jsonify({"weapons": weapon})
				elif  weapon[i]['stock'] < request_data['stock']:
					deleted_weapon = weapon.pop(i)
					return  jsonify({"deleted weapon" : deleted_weapon})
			else:
				return  "this weapon is out of stock"

> **"name"과 "stock"을 json으로 입력받아 기존 weapon 자원에 존재한다면 입력받은 stock만큼 stock을 조정하고 삭제 요청 수량이 기존 수량보다 많다면 아예 weapon 자원에서 삭제한다. 수량이 조정되었다면 조정 된 weapon자원의 상태를 반환하며 삭제되었다면 삭제된 내용을 반환한다.**
### 입력:
    {
		"name" : "test weapon",
		"stock" : 1
	}
### 출력:
    {
		"name" : "test weapon",
		"stock" : 1
	}
