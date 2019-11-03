from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django import forms
# Create your models here.



    
class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    ca_name  = models.CharField(max_length=300)
    college_name  = models.CharField(max_length=200)
    year  = models.CharField(max_length=300)
    sex = models.CharField(max_length=10)
    dob = models.CharField(max_length=100)
    txid = models.CharField(max_length=100,null=True,blank=True)
    num_events = models.IntegerField(default=0)
    course = models.CharField(max_length=100)
    accomodation = models.BooleanField(default=False)
    event_nirman = models.BooleanField(default=False)
    event_questionnaire = models.BooleanField(default=False)
    event_delta = models.BooleanField(default=False)
    event_this_way_that_way = models.BooleanField(default=False)
    event_mudmarine = models.BooleanField(default=False)
    event_colloquium = models.BooleanField(default=False)
    event_enviro = models.BooleanField(default=False)
    event_icreate = models.BooleanField(default=False)
    event_idp = models.BooleanField(default=False)
    team_nirman = models.BooleanField(default=False)
    team_questionnaire = models.BooleanField(default=False)
    team_delta = models.BooleanField(default=False)
    team_this_way_that_way = models.BooleanField(default=False)
    team_mudmarine = models.BooleanField(default=False)
    team_colloquium = models.BooleanField(default=False)
    team_enviro = models.BooleanField(default=False)
    team_icreate = models.BooleanField(default=False)
    team_idp = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=100)
    shilpid = models.CharField(max_length=100)
    payment_verified = models.BooleanField(default=False)
    txid_submitted = models.BooleanField(default=False)
    payment_plan = models.CharField(max_length=100)
    tshirt = models.BooleanField(default=False)
    events_locked = models.BooleanField(default=False)
    plan_locked = models.BooleanField(default=False)
    money = models.CharField(max_length=100)


    def __str__(self):
        return self.shilpid

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    event = models.CharField(max_length = 100)
    member1 = models.CharField(max_length=100)
    member2 = models.CharField(max_length=100)
    member3 = models.CharField(max_length=100)
    member4 = models.CharField(max_length=100)
    member5 = models.CharField(max_length=100)
    member6 = models.CharField(max_length=100)
    def __str__(self):
        return self.team_name + " " + self.member1



