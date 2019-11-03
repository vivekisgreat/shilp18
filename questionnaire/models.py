from django.db import models
from django.utils import timezone
import random
from ckeditor.fields import RichTextField


class Ans_chosen(models.Model):
    ques_id = models.IntegerField()
    ans = models.CharField(max_length = 10) 
    def __str__(self):
        return str(self.ques_id) + " "+ str(self.ans)

class Question(models.Model):
    ques = RichTextField()
    option1 = models.CharField(max_length=500,null=True,blank = True)
    option2 = models.CharField(max_length=500,null=True,blank = True)
    option3 = models.CharField(max_length=500,null=True,blank = True)
    option4 = models.CharField(max_length=500,null=True,blank = True)
    ans = models.CharField(max_length = 10)

    class Meta:
        ordering = ('id',) 

    def __str__(self):
        return str(self.id)

class Quiz_Team(models.Model):
    teamid = models.CharField(max_length = 100)
    team_name = models.CharField(max_length=100)
    leader_email = models.CharField(max_length = 100)
    password = models.CharField(max_length=10)
    number_members = models.IntegerField()
    not_submitted = models.BooleanField(default = True)
    score = models.IntegerField(default=0)
    allquestions = models.ManyToManyField(Question,default=None,blank=True)
    allanswers = models.ManyToManyField(Ans_chosen,default=None,blank=True)

    def __str__(self):
        return self.teamid + " " + self.team_name
    class Meta:
        ordering = ('-teamid',) 

class Team_member(models.Model):
    quiz_team  = models.ForeignKey(Quiz_Team , on_delete=models.CASCADE )
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    college = models.CharField(max_length = 100)
    year = models.CharField(max_length=20)
    mail_sent = models.BooleanField(default=False)
    def __str__(self):
        return self.name+" "+self.email+ " " + self.quiz_team.team_name



# allteams = Quiz_Team.objects.all()
    
# for teams in allteams:
#     allq = teams.allanswers.all()
#     for ques in allq:
#         teams.allanswers.remove(ques)
#     teams.save() 