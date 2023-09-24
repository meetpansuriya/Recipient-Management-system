from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.ImageField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()