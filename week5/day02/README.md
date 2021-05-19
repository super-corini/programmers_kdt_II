# **Day02 - Django로 동적 웹 페이지 만들기**

## **필수과제 : 재고 관리 List 구현하기**
<img src='../image/day02.gif' height = 300>
<br><br><br><br><br><br>

### **Buger 재고관리 section 만들기**
<br>

```html
{% for buger in buger_list %}
    {% if buger.set_menu %}
        <div style="font-family: serif;">{{ buger.name }}, coke(2000) : {{buger.price|add:2000 }}</div>

    {% else %}
        <div style="font-family: serif;">{{ buger.name }} : {{buger.price }}</div>

    {% endif %}
        
{% endfor %}
```

template 태그를 이용하여 `Buger`의 데이터를 받아왔고,
`{% if %}`를 통해 `set_menu`를 선택했을 시 `coke(2000원)`을 추가해주었다.
`coke`를 추가해주는 부분은 `add` 필터를 사용하였다.

<br>
<hr>
<br>

## **보너스 과제 : form을 이용해서 CUD 구현**
<br><br>

## *준비중*