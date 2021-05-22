from django.db import models

# Create your models here.
class Game(models.Model) :
    title = models.CharField(default="", max_length=75)
    platform = models.CharField(default="", max_length=15)
    genre = models.CharField(default="", max_length=15)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    reserved = models.IntegerField(default=0)
    extinct = models.BooleanField(default=False)

    def __str__(self) :
        return '{} ({})'.format(self.title, self.platform) 

    @property
    def to_list_without_ext(self) :
        return [self.id, self.title, self.platform, self.genre, self.price, 
                self.stock, self.reserved]
    
    def get_all_fields(self) :
        return self.id, self.title, self.platform, self.genre, self.price, \
                self.stock, self.reserved, self.extinct
