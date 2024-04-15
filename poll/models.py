from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=100)
    eid =models.CharField(max_length=100)
    dob=models.DateField(null=True,blank=True)
    address= models.TextField(max_length=300)
    email=models.EmailField(blank=True)
    mob=models.IntegerField(null=True,blank=True)

    