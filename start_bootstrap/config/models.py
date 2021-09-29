from django.db import models

# Create your models here.

class bootstrap_user(models.Model):
    name = models.CharField(max_length=100)
    image= models.ImageField(upload_to="static/assets/img")
    discription = models.TextField()
