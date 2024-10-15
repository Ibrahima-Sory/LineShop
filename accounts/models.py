from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class UserShop(AbstractUser):
    username = None 
    email = models.EmailField(unique=True, blank=True, null=True )
    phone = models.CharField( max_length=9 , unique=True, blank=True, null=True )
    adresse = models.CharField(max_length=55,blank=True, null=True )
    first_name = models.CharField(max_length=50 , blank=True, null=True )
    last_name = models.CharField(max_length=25, blank=True, null=True )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name 
