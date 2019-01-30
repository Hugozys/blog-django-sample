from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SECRET = 'S'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (SECRET,'Secret')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default=SECRET,
    )
    facebook = models.CharField(max_length=255,blank=True)
    instagram = models.CharField(max_length=255,blank=True)
    wechat = models.CharField(max_length=255,blank=True)
    website =models.CharField(max_length=255,blank=True)
    bio = models.CharField(max_length=5000, blank=True)
    live_place = models.CharField(max_length=255,blank=True)
    pass

