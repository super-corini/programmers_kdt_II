# 빅수비씨 사용 설명서

`GET, /whoami` 빅수비의 이름을 반환합니다

`GET, /echo?string={명령어}` 명령어를 입력하면 빅수비가 명령어를 반환합니다.

`GET, /weapon` 등록된 전체 무기들

`POST, /weapon`
`{ "name":{변경할 이름}, "stock":{변경할 수량} }` json 형식으로 등록 가능

`PUT, /weapon?name={무기이름}` 무기 이름을 찾고

`{ "name":{변경할 이름}, "stock":{변경할 수량} }` json 형식으로 넘겨주면 수정 가능

`DELETE, /weapon?name={무기이름}` 무기 이름을 통해 무기 삭제 가능
