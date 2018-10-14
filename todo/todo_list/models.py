from django.db import models
from django.forms import forms
# Create your models here.
class User(models.Model):
    email=models.EmailField()
    password = models.CharField(max_length=16)
    name=models.CharField(max_length=20,default='name')
    desg=models.CharField(max_length=25,default='Developer')
class List(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    def __str__(self):
        return self.item+' | '+str(self.completed)