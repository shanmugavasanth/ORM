# Ex02 Django ORM Web Application
## Date: 18/10/2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import Football_Player,Football_PlayerAdmin
admin.site.register(Football_Player,Football_PlayerAdmin)

model.py
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
```
## OUTPUT

![Alt text](<Screenshot 2023-10-13 183330.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
