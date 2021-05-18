# 빅수비 코어 api
### weapon api는 /weapon/에 구성되어있음
* Create : POST 메서드와 함께 json 형태로 된 바디를 전송하면 db에 자동으로 등록됨
  * model형태 : { "name" : "무기이름", "stock" : 0(숫자) }
* Read : weapon에서 GET 메서드로 리퀘스트를 하면 json 형태로 모든 db 데이터를 반환함
* Update : weapon에서 PUT 메서드와 함께 json 형태로 데이터를 전송하면 name에 해당하는 db를 검색, stock의 수치를 조정함
* Delete : weapon 에서 json형식의 name과 함께 DELETE메서드로 요청하면 해당하는 name의 데이터를 삭제하고 전체데이터를 반환함