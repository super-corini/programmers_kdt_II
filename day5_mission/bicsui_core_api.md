# API

## /whoami
method: GET  
github id와 name을 json 형태로 반환한다.
```
{
    "name": "DoHoon Song",
    "id": "dohoonsong"
}
```


## /echo?string=echoString
method:GET  
string에 대한 값을 json 형태로 반환한다.  
```
{
    "value": "echoString"
}
```

# CRUD
자원 weapon(name, stock)에 대한 CRUD를 구현  

## Create
새로운 weapon을 추가한다.  
name과 stock을 입력받는다.  
새롭게 추가된 weapon의 id를 반영하여 반환한다.

## Read
현재 존재하는 weapons를 반환한다. count를 통해 개수를 같이 출력.

## Update
현재 존재하는 weapon에 대한 정보를 변경.  
대상의 지정은 id를 기반으로 한다.  
name 또는 stock을 입력받아 변경한다.  

## Delete
현재 존재하는 weapon에 대한 정보를 삭제한다.
대상의 지정은 id를 기반으로 한다.  
삭제가 되었으면 deleted를 True로 포함한 weapons 목록을 다시 반환한다.
해당 id가 없으면 삭제가 되지 않고 deleted를 False로 반환한다.