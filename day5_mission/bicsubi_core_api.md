메인 페이지(./)
- "WEEK4 DAY5" 텍스트를 출력

깃헙 아이디 확인(./whoami)
- {name: <my id>} 형태로 출력

url에 입력한 string 출력(./echo?string="string")
- "string"에 해당하는 문자열 출력

무기 리스트 확인(./weapons)
- 무기 리스트를 출력

무기 추가(./weapons)
- 무기의 name, stock을 입력하면 무기 리스트에 무기를 추가하고 그 무기 정보 출력

무기 업데이트(./weapons/<int:weapon_id>)
- 무기 정보를 입력하면 업데이트되고 결과 출력

무기 삭제(./weapons/<int:weapon_id>)
- 무기를 삭제하고 삭제한 무기 정보 출력
