from django.db import models

# Create your models here.
'''
각 attribute 는 실제 데이터의 column(field) 이 된다.
class 를 바탕으로 만들어진 객체는 하나의 row가 된다.
'''
class Coffee(models.Model):
    def __str__(self): # coffee 객체를 호출할 때, self.name 을 호출하게 한다.
        return self.name
    # Field 1
    # Field 2
    name = models.CharField(default = "", max_length=30) 
    # default: 처음 모델의 행을 만들 때, 기본적으로 들어있는 값이 지정해줄 수 있따.
    # null: false 일 땐, 반드시 값이 채워져야한다는 것을 의미, default 는 false이다.
    # 이 외에도 unique , .. 등이 있다.
    price = models.IntegerField(default = 0)
    is_ice = models.BooleanField(default = False)

    '''
    문자열 : CharField
    숫자 : IntegerField, SmallIntergerField, ...
    논리형 : BooleanField
    시간/날짜 : DateTimeField
    ...
    '''
