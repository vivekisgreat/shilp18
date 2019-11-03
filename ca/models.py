from django.db import models
from django.utils import timezone


class Ca(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    gender = models.CharField(max_length=20)
    college = models.CharField(max_length=100)
    year = models.IntegerField()
    comment = models.CharField(max_length=5000)
    image = models.FileField(null=True)
    points = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-points',) 

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=5000)
    def __str__(self):
        return self.name
    