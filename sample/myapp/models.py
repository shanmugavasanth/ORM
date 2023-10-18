from django.db import models
from django.contrib import admin
class Football_Player (models.Model):
    name=models.CharField(max_length=120)
    age=models.IntegerField()
    phonenumber=models.IntegerField()
    dob=models.DateField()
    email=models.EmailField()
class Football_PlayerAdmin(admin.ModelAdmin):
    list_display=('name','age','phonenumber','dob','email')
    

