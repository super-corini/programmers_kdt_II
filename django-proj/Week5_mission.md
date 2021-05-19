# &#128161; Week5_Day1_mission

## /introduce/

### <code>introduce.html</code>

- Bootstrap 을 활용했습니다.
- 나중에 포트폴리오 용도로 쓰거나 참고할 수 있게 해당 내용을 담아보려 했습니다.
- 사진 사이즈나 자세한 내용은 아직 제대로 정리하기엔 시기상조인 것 같아 과정 후반부 쯤에 다시 정리할 예정입니다!!



# &#128161; Week5_Day2_mission

## &#128204; Burger

- burger model 을 만들어 CUD를 구현하였습니다.



<code>buger()</code> - id(pk), name, price, is_set

- id: primary key
- name: burger name
- price: burger price
- is_set: check is set



<code>burger.html</code>

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Burger List</title>
    </head>

    <body>
        <h1>My Burger List</h1>
        {% for burger in burger_list %}
            <p>Burger ID: {{ burger.id }}</p>
            <p>Burger name: {{ burger.name }}</p> 
            <p>Burger price: {{ burger.price  }}</p>
            <p>Set</p>: {{ burger.is_set }}</p>
        {% endfor %}

        <br/>
        <br/>

 
        <form method="POST" >
            {% csrf_token %}
            <button type = "submit">New Burger Add</button>
        </form>


    </body>


</html>
```

- 등록된 burger 들의 전체 메뉴를 보여주는 main page 입니다.
- <code>{% csrf_token %}</code> : django에서 post 방식으로 데이터를 전송할 때 기본으로 제공하는 보안수단이다.

<br/>

<code>create.html</code>

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Burger Update</title>
    </head>

    <body>
        <h1>Update Burger Info</h1>
        <form method="POST">
            {% csrf_token %}
            {{ burger_form.as_p }}
            <button type = "submit">Save</button>
            </form>
    </body>


</html>
```

- burger를 새로 등록할 때 사용하는 page 입니다.

- <code>{{ forms.as_p}}</code>: 폼의 각 필드를 p 태그 안에서 레이블과 텍스트로 배치한다.

<br/>

<code>update.html</code>

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Burger Update</title>
    </head>

    <body>
        <h1>Update Burger Info</h1>
        <form method="POST">
            {% csrf_token %}
            {{ burger_form.as_p }}
            <button type = "submit">Save</button>
            </form>
    </body>


</html>
```

- burger를 새로 update 할 때 사용되는 page 입니다.

<br/>

<code>burger_view()</code>

```python
def burger_view(request):
    if request.method =="POST":
        return redirect('create')

    burger_all = Burger.objects.all()
    form = BurgerForm()
    return render(request, 'burger.html', {"burger_list": burger_all,
                                                "burger_form": form})
```

- 현재 등록된 burger 들을 보여주기 위해 render 로 전달하는 함수입니다.
- burger.html 을 호출합니다.
- <code>New Burger Add</code> 버튼을 누르면 <code>create.html</code> 로 이동합니다.

<br/>

<code>create()</code>

```python
def create(request):
    if request.method == "POST": # method가 post 일 때
        form = BurgerForm(request.POST)
    
        if form.is_valid(): # form 유효성 검증
            form.save() # 저장
            return redirect('main') # 다시 main 으로
    else:
        form = BurgerForm() # 빈 form 열기
    return render(request, 'create.html', {'burger_form' : form})
```

- <code>request.method == 'POST'</code> 일 경우, <code>form</code> 을 받아와서 유효하다면 저장한다. 이후 <code>redirect</code> 를 통해 main page 로 이동한다.
- <code>'POST'</code> 방식이 아니라면 (페이지를 처음 열었으면), <code>BurgerForm</code>을 열어준다.

<br/>

<code>update(pk)</code>

```python
def update(request, pk):
    burgers = get_object_or_404(Burger, pk=pk)
    if request.method =='POST':
        form = BurgerForm(request.POST, instance=burgers) # burger 객체 가져오기
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = BurgerForm(instance = burgers) # buger 객체 가져와서 form 을 생성
    return render(request, 'update.html', {'burger_form': form})
```

- pk 의 값에 해당하는 instance 를 받아온다. 이 후 해당 instance 를 새로 update 한다.

<br/>

<code>delete(pk)</code>

```python
def delete(request, pk):
    burgers = Burger.objects.get(pk=pk)
    burgers.delete()
    return redirect('main')
```

- pk 에 해당하는 instance 를 삭제한다.



<br/>

<code>forms.py</code>

```python
# form 이라는 모듈을 import
from django import forms
# Model 호출
from .models import Burger

# ModelForm 을 상속받는 BurgerForm 생성
class BurgerForm(forms.ModelForm):
    class Meta:
        model = Burger
        fields = ('id', 'name', 'price', 'is_set')


```

- <code>from django import forms</code>: django 가 기본적으로 제공하는 forms 모델을 import 한다.

- <code>from .models import Burger</code>: Burger 모델 을 import
- <code>forms.ModelForm</code>: 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성

<br/><br/>

## &#128161; Check Point

- PUT 과 DELETE 를 핸들링하는 것을 해결하지 못했습니다...
- 일단은 POST 방식으로 새 페이지를 열거나 우회하는 식으로 동작을 했기에 이를 추후에 다시 도전해볼 생각입니다.
- 현재 urls 로 넘겨줄 때, 인자를 같이 넘겨주고 싶었는데 해당 코드를 구현을 하지 못하여 고민중에 있습니다. 

> &#128173; burger/update/2 를 가고 싶을 때, 2 라는 pk 값을 main page 에서 button 을 눌렀을 때 redirect('update' + str(pk)) 식으로 넘겨주고 싶은데 해당 기능을 구현하지 못하여 조금 더 학습 후에 도전해보겠습니다!!