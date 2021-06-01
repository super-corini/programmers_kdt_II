## Basic API
`GET /whoami`  
GitHub 이름 출력
```json
{
  "name" : "Druwa-git"
}
```
`GET /echo?string="string"`  
string은 어떤 형태로 넘기든 상관없음
```json
{
   "value" : "string"
}
```

## Weapon Master API
`GET /weapon`  
입력없이 List 출력
```json
{
   "weapons" : [ weapon_list ]
}
```
`POST, PUT method는 다음과 같은 형식으로 API를 넘겨야 함`
```json
{
   "name" : string,
   "stock" : integer
}
```

`POST /weapon`
```json
{
   "weapon" : return_created_weapon
}
```
`PUT /weapon/"id"`
```json
{
   "weapon" : return_updated_weapon
}
```
`DELETE /weapon/"id"`
```json
Success

or

Fail
```