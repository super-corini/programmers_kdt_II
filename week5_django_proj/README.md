# Week5 Day1 - Django로 자기소개 페이지 만들기

### 필수 과제 : 아이엠 그라운드 자기소개 하기

- 다음 요청을 처리하는 웹 어플리케이션을 제작해주세요.
- `GET /` → **자기소개 웹 페이지**를 Response
    - 이 페이지는 HTML을 이용해서 여러분이 원하는 내용을 작성해주세요.

### 보너스 과제 : ⭐️아이😊엠 그라운드⛳️ 자기💁‍♀️소개💁‍♂️ 하기⭐️

- CSS나 JavaScript를 이용해 자신의 웹 페이지를 더욱 멋있게 만들 수 있습니다. HTML으로만 된 밋밋한 자기소개 페이지를 꾸며봅시다.
- 이들을 사용하기 위해선 이 파일들이 담긴 경로를 [STATIC_URL](https://docs.djangoproject.com/en/3.1/howto/static-files/)을 이용해 지정해주어야합니다.

---

# Week5 Day2 - Django로 동적 웹 페이지 만들기

### 필수 과제 : 재고 관리 List 구현하기

- 다음 요청을 처리하는 웹 어플리케이션을 제작해주세요.
- `GET /` : Day 3에서 만든 자기소개 웹 페이지를 Response
- django를 바탕으로 재고 관리를 진행하는 Website를 만들고자 합니다.
    1. 재고관리를 하고자 하는 대상을 하나 정해주세요. (coffee, burger, )
    2. 이 대상에 맞는 Database Scheme를 model로 하여 `model.py` 에 작성합니다. 
    아래 예시에서는 coffee 재고 관리 리스템이라는 가정하에 서술합니다.
    3. 이를 바탕으로 다음 기능을 구현해주세요.
        - `GET /coffees` : 커피 목록을 *unordered list*로 보여주기

### 보너스 과제 : form을 이용해서 CUD구현하기

HTML의 `form` 을 이용해서 우리는 정보를 클라이언트단에서 서버단으로 전달할 수 있는데요, 이 정보를 바탕으로 다음 기능을 admin page가 아닌, `/coffees` 페이지에서 진행할 수 있도록 만들어봅시다.

다음 기능을 구현해주세요. 필수 과제 부분을 완성한 후에 구현하셔야합니다.

- `POST /coffees`  : 새로운 커피를 추가
- `PUT /coffees/<pk>` : 해당하는 커피의 정보를 변경
- `DELETE /coffees/<pk>` : Primary Key값에 해당하는 커피를 제거
- `POST`, `PUT`, `DELETE`를 진행하고 난 후에는 커피 목록을 *unordered list*로 보여주기
- `redirect()` 함수가 필요할 수 있습니다. 이는 인자에 해당하는 URL로 이동합니다. (그에 해당하는 views가 실행될 수도 있습니다.)


[5주차] 이민혁
- day1 mission. mandatory / ​bonus
  - Django기반 자기소개 페이지 만들기  
    - static 파일을 이용하여 css, js img를 자기소개에 넣어보았습니다.
    - css는 간단하게 이해하며 작성해 보았고,
    - js는 typewriter를 사용합니다. 제가 작성한 코드가 아니며 조금 변형했고, 연동하는 것에 의의를 두었습니다.
- day2 mission 1. mandatory / bonus
  - 재고관리 List / form 을 이용한 CUD
    - Burger model을 만들어 burger에 관련한 CUD를 구현했습니다.
      - burger : id(pk), name, price
    - `GET /burgers`:  
      - `for`와 `<li>` tag를 이용하여 unorderd list를 구현했습니다.
      - url 요청을 받으면 view의 `burgers_view_unorded()`가 호출됩니다.
    - `POST /burgers`  
      - page에 Burgerform을 활용하여 사용자에게 데이터를 입력받아 burger menu를 추가합니다.
      - url 요청을 받으면 view의 `burgers_view_unorded()`가 호출됩니다.
    - `PUT /burgers/<int:pk>`
      - pk의 정보로 burger 정보를 변경합니다.
      - request body에 json의 형태로 데이터가 전달되는 것으로 가정했습니다.
        - ex { "name": "stacker burger", "price": 6000}
      - url 요청을 받으면 view의 `burgers_post_delete()`가 호출됩니다.
      - redirect() 를 이용해 '/burgers'로 redirect 되고 수정된 결과를 unodered list로 보여줍니다.
    - `DELETE /burgers/<int:pk>`
      - pk의 정보로 burger 정보를 삭제합니다.
      - url 요청을 받으면 view의 `burgers_post_delete()`가 호출됩니다.
      - redirect() 를 이용해 '/burgers'로 redirect 되고 수정된 결과를 unodered list로 보여줍니다.

- 진행중인 task
  - week4 day5 extra mission이 아직 남았습니다.
- 이전 comment에 남겼던 aws ec2에서 flask를 background로 돌리는 것에 대한 조언을 구했었는데요,  
이번 monthly project가 cloud server에서 django project를 배포 하는 것인줄 몰랐습니다.
  조금 더 고민하면서 Monthly project를 멋있게 해내겠습니다.!