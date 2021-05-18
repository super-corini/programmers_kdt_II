from django.db import models

class Burger(models.Model) : #{
    name  = models.CharField(default="", null=False, max_length=30, )
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    def __str__(self) : #{
        return self.name    
    #}
#}
