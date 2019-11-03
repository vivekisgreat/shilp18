from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Event(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    prize1 = models.CharField(max_length=100)
    prize2 = models.CharField(max_length=100)
    prize3 = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    pslink = models.CharField(max_length=200)
    is_workshop = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    

class Detail(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    detail = RichTextField()	
    rank = models.IntegerField()

    def __str__(self):
        ev = self.event
        name = ev.name
        return (name + str(self.rank))

    class Meta:
        ordering = ('event','rank',) 

 
    

