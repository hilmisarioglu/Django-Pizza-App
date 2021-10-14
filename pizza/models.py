# Create your models here.
from django.db import models


class Pizza(models.Model):
    SIZE = (
            ('SMALL' , 'Small'),
            ('MEDIUM' , 'Medium'),
            ('LARGE' , 'Large'),
    )
    Topping1 = models.CharField(max_length=200)
    Topping2 = models.CharField(max_length=200)
    Size = models.CharField(max_length=10, choices=SIZE)
    
    def __str__(self):
        return self.Topping1 + ' ' +self.Topping2+ ' ' + self.Size
