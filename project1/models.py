from django.db import models

# Create your models here.
class Feature(models.Model):
    # id: int
    # name:str
    # details:str
    name= models.CharField(max_length=100)
    details= models.CharField(max_length=500)

class Feature1(models.Model):
    name= models.CharField(max_length=100)
    details= models.CharField(max_length=500)

class Feature2(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

