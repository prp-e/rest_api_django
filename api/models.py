from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Article(models.Model):
    title   = models.CharField(max_length=250) 
    text    = models.TextField() 
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
    