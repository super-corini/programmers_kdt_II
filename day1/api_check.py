"""
requests를 사용해서 postman의 RESTAPI command 구현했습니다.
"""
# flask data 확인용
import requests
import json

# url
url = "http://127.0.0.1:5000"


# 기본 url의 내용이랑 응답 확인
def get_hello():
    response = requests.get(url)
    return response.content.decode(), response.status_code


#  /menus 내용
def get_menus():
    """
    content.decode()는 raw 파일 받아서 decode해서 str이고,
    json()은 내용이 json이어서 파이썬에서는 dictionary로 바꿔줍니다.
    """
    url1 = url+'/menus'
    response = requests.get(url1)
    return [response.content.decode(), response.json()]


# /menus post하기1
def make_menus1(menu):
    """
    내부 라이브러리 json으로 menu를 json 파일로 바꿔준 후,
    type을 json으로 설정해서 post해줍니다.
    (postman에서 post 코드 볼 수 있긴 한데, 깔끔하지 않아서 시도해봤습니다.)
    """
    url1 = url+'/menus'
    response = requests.post(url1,
                             data=json.dumps(menu),
                             headers={'Content-Type': 'application/json'}
                             )
    return response.status_code


# /menus post하기2
def make_menus2(menu):
    """
    requests에서 version update와 함께
    header의 type 설정과 data 변환 과정을 json= 으로 끝낼 수 있습니다.
    """
    url1 = url+'/menus'
    response = requests.post(url1, json=menu)
    return response.status_code


def update_menu(id_no, menu):
    url1 = url+'/menus'+'/{}'.format(id_no)
    response = requests.put(url1, json=menu)
    return response.status_code


def remove_menu(id_no):
    url1 = url+'/menus'+'/{}'.format(id_no)
    response = requests.delete(url1, json=menu)
    return response.status_code


if __name__ == "__main__":
    """ 테스트용
    print(get_hello())
    print(get_menus()[0])  # type: # json
    print(get_menus()[1])  # type: # dictionary
    """

    menu1 = {
        "name": "Dolce Latte",
        "price": 5400
    }

    menu2 = {
        "name": "Dolce Latte",
        "price": 5400
    }

    menu3 = {
        "name": "Milk Milk Latte^^",
        "price": 9900
    }

    menu4 = {
        "name": "DolDolce Latte",
        "price": 9800
    }

    print(make_menus2(menu1))
    print(make_menus2(menu2))
    print(update_menu(3, menu3))
    print(remove_menu(1))
    print(update_menu(4, menu4))