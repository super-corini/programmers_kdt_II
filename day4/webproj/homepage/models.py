from django.db import models

# Create your models here.

# 하나의 객체(Object)는 DB의 각각 행(row)
class Coffee(models.Model):
    
    # field = models.FieldType()....
    # 각각의 필드(Field)는 DB의 각각 열(column)
    """ field의 타입
    문자열 : CharField()
    숫자 : IntegerField()
    논리형 : BooleanField()
    시간/날짜 : DateTimeField()
    """

    def __str__(self):  # 클래스 기본 출력 형식 메서드
        return self.name
    
    # id값은 자동으로 들어간다.
    name = models.CharField(default='', max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)
