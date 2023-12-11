from django.db import models

# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=250)
    year = models.IntegerField()
    
    def __str__(self):
        return f'{self.model} {self.year}'
    
    