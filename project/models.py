from curses.ascii import US
from django.db import models

# Create your models here.
class User():
    UserName = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Gender = models.CharField(max_length=6)
    PhoneNumber = models.CharField(max_length=14)
    Age = models.IntegerField()
    Username = models.CharField(max_length=15, unique=True)

class Account(User):
    Username = models.ForeignKey(User)
    Password = models.CharField(max_length=20)
    