# &#128161; API

## &#128204; /whoami
<code>method: GET</code> 
<code>github_id</code>와 <code>name</code>을 <code>json</code> 형태로 반환한다.

```
{
    "id": "yn-e-si",
    "name": "Jinyong Lee"
}
```

<br/>

## &#128204; /echo?string=echoString

<code>method:GET</code> 
<code>string</code>에 대한 값을 <code>json</code> 형태로 반환한다.  

```
{
    "value": "echoString"
}
```

<br/>



# &#128161; CRUD

자원 weapon(name, stock)에 대한 <code>CRUD</code>를 구현한다.



<br/>

## &#128204; Create
- 새로운 weapon을 추가한다. 
- name과 stock을 입력받는다. 
- 새롭게 추가된 weapon을 리턴한다.

<br/>



## &#128204; Read
- 현재 존재하는 weapons를 반환한다.

<br/>

## &#128204; Update
- 현재 존재하는 weapon에 대한 정보를 새로 변경해준다.
- 변경하고자 하는 weapon은 weapon의 <code>name</code> 으로 지정해준다.
- 이후 새롭게 변경하고자 하는 <code>name</code> 과 <code>stock</code> 을 입력받아 새로 변경해준다.

## &#128204; Delete
- 현재 존재하는 weapon에 대한 정보를 삭제해준다.
- 삭제고하자 하는 weapon 은 weapon 의 <code>name</code>으로 지정해준다.
- 중복되는 <code>name</code> 이 있다면 해당 <code>name</code>의 <code>weapon</code> 을 전부 삭제해준다.