1. 서비스 설명서 

0 . 만든이 서비스 
    0.1 API 서비스 정보
        - api명  : 정말 대단한분
        - api 설명 : 이서비스를 만든 천재
    0.2 API 서비스 보안적욘 기술 수준
        - 서비스 인증 권한 : 그런거없음
        - 메시지 레벨 암호화 : 그런거 안키움
        - 전송 레벨 암호화 : 안함 느려짐
        - 인터페이스 표준 : 모름
        - 교환데이터 표쥰 : html, xml, json
    0.3 서비스 배포 정보 
        - 서비스 url : https://topknell.tistory.com/
        - 서비스 명세 URL : 없음
        - 서비스 버전 : 0.000001
        - 서비스 시작일 : 오늘
        - 메시지 교환 유형 : request-Response
        - 서비스 제공자 : 아기새
        - 데이터 갱신주기 : 님이 하셈
    1. 요청 메시지 명세
        -  url 접속(/whoami) get 방식
    2. 응답메시지 명세
        - 항목명 : 깃 아이디 
        - 항목크기 : 작지않음
        - 항목구분 : 1등급
        - 샘플데이터 : liebespaar93
        - 항목설명 : git 아이디임
    3. 메시지 예제
        - 요청 : 0.0.0.0:5000/whoami
        - 응답 : <respons>index.html,{'name_h':liebespaar93}</respons>
        - 주의 : 꼭 웹으로 실행할것

1.1 로그인 서비스
    -짜잘한것 위와 비슷함

    1. 요청 메시지 명세
        - url 접속 (/echo?접속자쓰고싶은거) get 방식
    2. 응답메시지
        - 항목명 : 여러가지
        - 항목크기 : 좀많음
        - 항목구분 : 1등급
        - 샘플데이터 : #아까보넨이름#  heroname_h = 접속자 쓰고싶은거 ,weaponlist_h <== 이거는 {[{'id':1,'name':'초급자 단검', 'stock': 1 }]}
        - 항목 설정 로그인한거임
    3. 메시지 예제
        - 요청 : 0.0.0.0:5000/echo?heroname="접속자쓰고싶은거"
        - 응답 : <respons>login.html,{'heroname_h':접속자쓰고싶은거, 'weaponlist_h':[{'id':1,'name':'초급자 단검', 'stock': 1 }]}</respons>
        - 주의 : 제발 웹으로 편하게 보셈
        
2. weapon 컨트롤
    -짜잘한것 위와 비슷함
    1. 요청 메시지 명세
        - url 접속 (/weaponlist/<이부분 view, create, update, delete 사용가능>)
        - create, update 할경우  form[{'lid':값,'lname':값,'lstock':값}]를 추가하여보넬것
        - delete 할경우 form[{'lid':값}]을 추가하여 보넬것
    2. 응답 메시지 
        - 항목명 : 여러가지
        - 항목크기 : 좀큼
        - 항목구분 : 1등급
        - 샘플데이터 :weaponlist_h <== 이거는 {[{'id':1,'name':'초급자 단검', 'stock': 1 }]}
    3. 메시지 예제
        - 요청 : 0.0.0.0:5000/weaponlist/<할명령어>?<필요하면 form={'lid':값,'lname':값,'lstock':값}>"
        - 응답 : <respons>login.html,{'weaponlist_h':[{'id':1,'name':'초급자 단검', 'stock': 1 }]}</respons>
        - 주의 : 제발 웹으로 편하게 보셈

API 서비스 정보 []