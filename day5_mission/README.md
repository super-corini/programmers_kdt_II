# Core Mission

- 제출할 파일 : <span style="background-color: #E46C76">bicsubi_core_api.md</span> , API 구축에 사용되는 파일들
Marked text
- 다음의 명세에 맞게 API를 작성합니다.

    - <span style="background-color: #E46C76">GET /whoami</span>
        - 여러분의 github id를 반환합니다.
        - Example:
        ```json
        {
        "name" : "super-corini"
        }
        ```
    

    - <span style="background-color: #E46C76">GET /echo?string="string"</span>
        - Query String : <span style="background-color: #E46C76">string</span>
        - <span style="background-color: #E46C76">string</span> 을 반환합니다.
        ```json
        {
        "value" : "string"
        }
        ```
    

- 다음의 요구사항에 맞게 API를 설계하고 작성합니다.
    - 빅수비는 자원 <span style="background-color: #E46C76">weapon</span> 을 가집니다. 이 <span style="background-color: #E46C76">weapon</span> 은 이름(name : str)과 수량(stock : int)을 가지며 each 대해 Create, Read, Update, Delete를 진행할 수 있습니다.
        - Create : 새로운 <span style="background-color: #E46C76">weapon</span> 을 추가
        - Read : 현재 존재하는 <span style="background-color: #E46C76">weapon</span> 을 확인
        - Update : 현재 존재하는 <span style="background-color: #E46C76">weapon</span> 에서 특정 속성(이름, 수량)을 변경
        - Delete : 현재 존재하는 특정 <span style="background-color: #E46C76">weapon</span> 을 삭제

작성한 API에 대한 명세(API Docs)를 <span style="background-color: #E46C76">bicsubi_core_api.md</span> 에 작성하여 제출합니다.

모든 API는 작성자가 설계한대로 원활하게 동작되어야합니다.
