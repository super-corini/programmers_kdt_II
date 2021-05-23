from django.db import models

# Create your models here.
class Coffee(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(default="", max_length=30, null=False)
	price = models.IntegerField(default=0)
	is_ice = models.BooleanField(default=False)
	amount = models.IntegerField(default=0)
