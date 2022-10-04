from django.db import models

# Create your models here.
class CoffeeHouse(models.Model):
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    wifi = models.BooleanField(default=True)
    open_area = models.BooleanField(default=False)
    silence_area = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    celiac  = models.BooleanField(default=False)
    bike_friendly = models.BooleanField(default=False)
    price_rate = models.IntegerField(default=0, null=True, blank=True)
    toasters = models.BooleanField(default=False)
    origen = models.CharField(max_length=255, null=True, blank=True)
    machine = models.CharField(max_length=255, null=True, blank=True)
    coffee_image = models.ImageField(null=True, blank=True, upload_to="coffees_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering= ['-updated_at', '-created_at']
    
    def __str__(self):
        return self.name 
    
    
    
  