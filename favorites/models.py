from django.db import models
from coffeehouse.models import CoffeeHouse
from django.contrib.auth.models import User

class Favorite(models.Model):
    house = models.ManyToManyField(CoffeeHouse)
    name = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.house) 
    
    
    
  
