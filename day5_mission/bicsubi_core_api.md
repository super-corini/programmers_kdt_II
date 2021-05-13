# 빅수비 코어 API

## 빅수비 기본 기능

### /whoami
- 제작자의 github ID를 .json 형식으로 반환합니다.
````
{
    "name" : "fantasworm"
}
````
### /echo?string="string"
- "string"을  .json 형식으로 반환합니다.
- 예시: "string"에 무야호 입력 -> /echo?string=무야호
````
{
    "value" : "무야호"
}
````
## 빅수비 무기 CRUD 기능
### Create: POST /weapon
- Body의 .json대로 무기와 그 무기의 수량 등록
- 예시: 입력
````
{
	"name" : "Railgun",
	"amount" : 1
}
````
- 출력
````
{
	"amount": 1,
	"id": 2,
	"name": "Railgun"
}
````
### Read: /weapon
- 이미 등록된 무기와 그 수량을 모두 조회
- 예시
````
{
	"weapons": [
		{
			"amount": 2,
			"id": 1,
			"name": "Beam Saber"
		},
		{
			"amount": 1,
			"id": 2,
			"name": "Railgun"
		}
	]
}
````
### Update: PUT /weapon/id
- 이미 있는 id의 무기를 Body의 .json대로 정보 업데이트
- 예시: 입력(/weapon/1)
````
{
"name": "Beam Saber",
"amount": 4
}
````
- 출력 
````
{
	"amount": 4,
	"id": 1,
	"name": "Beam Saber"
}
````
### Delete: DELETE /weapon/id
- 이미 있는 id의 무기를 삭제
- 예시: (/weapon/2)
````
{
	"amount": 1,
	"id": 2,
	"name": "Railgun"
}
````
