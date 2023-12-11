from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=250)
    species = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.name} {self.species}"