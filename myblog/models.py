from distutils.command import upload
from email.mime import image
from wsgiref.simple_server import demo_app
from django.db import models
from django.contrib.auth.models import User 
import datetime as dt
from django.utils import timezone



class Post (models.Model):
    title = models.CharField(max_length=20)
    post = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField( blank=True, upload_to='images')

