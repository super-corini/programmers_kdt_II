from django.db import models

# Create your models here.
class Post(models.Model):

	title = models.CharField(max_length=100)
	author = models.CharField(max_length=10)
	date = models.DateTimeField(auto_now_add=True)
	content = models.TextField(default="")

	def __str__(self):
		return self.title