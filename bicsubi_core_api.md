week4_day5 Mission


```Python
@app.route('/whoami',methods=['GET'])
def get_whoami():
    return jsonify({"name":'changhyeonlee-0703'})
```
![image](https://user-images.githubusercontent.com/82853790/118227822-29095800-b4c4-11eb-911d-7fc425475f95.png)

```Python
@app.route('/echo/<Query>')
def echo_string(Query):
    echo = {
		"value" : Query
	}
    return jsonify(echo)
```

![image](https://user-images.githubusercontent.com/82853790/118227918-4e966180-b4c4-11eb-831a-60f4c794ef47.png)


```Python
@app.route('/weapon',methods=['GET'])
def read_weapon():
    #menus가 리스트 타입이라 json으로 변환할 수 없음
    sql = "SELECT * from bigsubi_weapon"
    cur.execute(sql)
    result = cur.fetchall()
    db.commit()
    return jsonify({"weapon":result})
```

![image](https://user-images.githubusercontent.com/82853790/118227983-6a016c80-b4c4-11eb-81f4-fc121eda220f.png)


```Python
@app.route('/weapon',methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    sql = "insert into bigsubi_weapon(name,stock) values (%s, %s)"
    cur.execute(sql, (request_data['name'], request_data["stock"]))
    sql_sel = "SELECT * from bigsubi_weapon"
    cur.execute(sql_sel)
    result = cur.fetchall()
    db.commit()
    return jsonify({"weapon": result})
```

![image](https://user-images.githubusercontent.com/82853790/118228049-869da480-b4c4-11eb-94b8-9ffb0446b863.png)



```Python
@app.route('/weapon',methods=['PUT'])
def update_weapon():
    request_data = request.get_json()
    sql = "update bigsubi_weapon set name = %s, stock= %s where name = %s"
    cur.execute(sql, (request_data['changed_name'], request_data['stock'],request_data['name']))
    sql_sel = "SELECT * from bigsubi_weapon"
    cur.execute(sql_sel)
    result = cur.fetchall()
    db.commit()
    return jsonify({"weapon": result})
```
![image](https://user-images.githubusercontent.com/82853790/118228103-9b7a3800-b4c4-11eb-9d18-226913cae319.png)


```Python
@app.route('/weapon',methods=['DELETE'])
def delete_weapon():
    request_data = request.get_json()
    sql = "DELETE FROM bigsubi_weapon WHERE name = %s"
    cur.execute(sql, (request_data['name']))
    sql_sel = "SELECT * from bigsubi_weapon"
    cur.execute(sql_sel)
    result = cur.fetchall()
    db.commit()
    return jsonify({"weapon": result})
```

![image](https://user-images.githubusercontent.com/82853790/118228164-b2208f00-b4c4-11eb-9400-0ce2661e1c95.png)




