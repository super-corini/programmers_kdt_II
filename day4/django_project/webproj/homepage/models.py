from django.db import models

# Create your models here.
class Coffee(models.Model):
	def __str__(self):
		return self.name
	id = models.AutoField(primary_key=True)
	name = models.CharField(default="", max_length=30)
	price = models.IntegerField(default=0)
	is_ice = models.BooleanField(default=False)
	"""
	문자열: CharField
	숫자: Integer, SmallInteger
	논리형: Boolean
	시간/날짜: DataTime
	"""