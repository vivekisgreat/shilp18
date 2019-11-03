from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from .models import *
from user.models import *
from django.contrib.auth.models import User, UserManager
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
from django.core.mail import send_mail, get_connection
import csv
import random
import datetime
import json

admin_email = ['Admin@shilpiitbhu.org','events@shilpiitbhu.org','questionnaire@shilpiitbhu.org','eventsteam@shilpiitbhu.org']
admin_password = ['shilp2018','eventsshilp','teamstark','teamstark']
my_host = 'smtp.zoho.com'
my_port = 587
my_use_tls = True
def registration(request):
    global admin_email,admin_password,my_host,my_port,my_use_tls
    if 'name1' in request.POST.keys():
        new_team = Quiz_Team()
        new_team.team_name=request.POST['teamname']
        new_team.leader_email=request.POST['email1']
        new_team.password=get_random_string(length=8)
        new_team.number_members=1
        new_team.teamid="1"
        new_team.save()
        new_team.teamid = 'TSH100'
        lenpk=4-len(str(new_team.pk))
        for i in range(lenpk):
            new_team.teamid = new_team.teamid+'0'
        new_team.teamid = new_team.teamid + str(new_team.pk)
        new_team.save()
        error = False
        member1 = Team_member()
        member1.name = request.POST['name1']
        member1.email = request.POST['email1'] 
        member1.phone = str(request.POST['phone1']) 
        member1.college = request.POST['college1'] 
        member1.year = request.POST['year1'] 
        member1.gender = request.POST['gender1']
        member1.quiz_team = new_team
        error_message = "Congratulations!! You have succesfully registered. Password and Team Id will be sent to the your registered Email Id within 24 hours"
        
        try:
            prev_member = Team_member.objects.get(email = member1.email)
            if prev_member.email == member1.email:
                error = True
            new_team.delete()
            return render(request,'questionnaire/registration.html',{'error_message':"One or more members have already registered",'success':False})
        except:
            c=0

        if error == False:
            member1.save()
            
        else:
            error_message = "One or Both the members have already registered"

        if request.POST['name2']!= '':
            error = False
            member2 = Team_member()
            member2.name = request.POST['name2']
            member2.email = request.POST['email2'] 
            member2.phone = str(request.POST['phone2']) 
            member2.college = request.POST['college2'] 
            member2.year = request.POST['year2'] 
            member2.gender = request.POST['gender2'] 
            member2.quiz_team = new_team 
            try:
                prev_member = Team_member.objects.get(email = member2.email)
                error = True
                member1.delete()
                new_team.delete()
                return render(request,'questionnaire/registration.html',{'error_message':"One or more members have already registered",'success':False})

            except:
                error = False

            if error == False:
                
                member2.save()
                title = 'Shilp : Registration for Questionnaire Succesful'
                content1 = "Hello " + member2.name + ",\n\nGreetings from Team Shilp!\n\nWe are happy to inform you that you have successfully registered for Questionnaire."
                content2 = "\nYour Team Name is :" + new_team.team_name + "\nYour TeamId is : "+ new_team.teamid+"\n"
                content3 = "\nYour Password is  : "+ new_team.password+"\n"
                content4 = "\n\nFeel free to explore our website for further details."
                content5 = "\n\nIn case you have not registered for the event or have any queries, feel free to contact us at admin@shilpiitbhu.org, we'll be happy to help you!\n"
                content6 = "\n\nBest Wishes,\nTeam Shilp\nIIT(BHU) Varanasi."
                content = content1 + content2 + content3 + content4 + content5 + content6
                
                for i in range(4):
                    try:
                        connection1 = get_connection(host=my_host, 
                            port=my_port, 
                            username=admin_email[i], 
                            password=admin_password[i], 
                            use_tls=my_use_tls) 
                        send_mail(title, content, admin_email[i] , [member2.email], fail_silently=False,connection = connection1)                        
                        member2.mail_sent = True
                        member2.save()
                        break
                    
                    except:
                        c=0
                     
       
        if error == False:

            currUser = User.objects.create_user(username=new_team.teamid, email=member1.email, password=new_team.password)
            currUser.save()
            for j in range(1,11):
                q = Question.objects.get(pk=j)
                new_team.allquestions.add(q)
            new_team.save()
            title = 'Shilp : Registration for Questionnaire Succesful'
            content1 = "Hello " + member1.name + ",\n\nGreetings from Team Shilp!\n\nWe are happy to inform you that you have successfully registered for Questionnaire."
            content2 = "\nYour Team Name is :" + new_team.team_name + "\nYour TeamId is : "+ new_team.teamid+"\n"
            content3 = "\nYour Password is  : "+ new_team.password+"\n"
            content4 = "\n\nFeel free to explore our website for further details."
            content5 = "\n\nIn case you have not registered for the event or have any queries, feel free to contact us at admin@shilpiitbhu.org, we'll be happy to help you!\n"
            content6 = "\n\nBest Wishes,\nTeam Shilp\nIIT(BHU) Varanasi."
            content = content1 + content2 + content3 + content4 + content5 + content6
            
            for i in range(4):
                    try:
                        connection1 = get_connection(host=my_host, 
                            port=my_port, 
                            username=admin_email[i], 
                            password=admin_password[i], 
                            use_tls=my_use_tls) 
                        send_mail(title, content, admin_email[i] , [member1.email],fail_silently = False, connection = connection1)
                        member1.mail_sent = True
                        member1.save()
                        break
                    except:
                        c=0

            
        # assign_ques(request,new_team)
        return render(request,'questionnaire/registration.html',{'error_message':error_message,'success':True})
    
    else:
        
        return render(request,'questionnaire/registration.html')



# downloading csv of data

def download_questionnaire(request):
    if not request.user.is_staff:
        return HttpResponse("Permission Denied")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="questionnaire_teams.csv"'
    allTeams = Quiz_Team.objects.all()
    writer = csv.writer(response)
    row = ['S No.']
    i=0
    for item in allTeams:
        if i==0:
            for attrib,value in item.__dict__.items():
                if attrib !='_state' and attrib !='id':
                    row.append(attrib.title())
            members = item.team_member_set.all()

            j=1
            for member in members:
                if j==1:
                    for attrib,value in member.__dict__.items():
                        if attrib != 'quiz_team_id' and attrib !='_state' and attrib !='id':
                            row.append(attrib+str(j))
                    for attrib,value in member.__dict__.items():
                        if attrib != 'quiz_team_id' and attrib !='_state' and attrib !='id':
                            row.append(attrib+str(j+1))
                j=j+1
            writer.writerow(row)
        i=i+1
        row = [i]
        for attrib,value in item.__dict__.items():
            if attrib !='_state' and attrib !='id':
                row.append(value)
        members = item.team_member_set.all()
        j=1
        for member in members:
            for attrib,value in member.__dict__.items():
                if attrib != 'quiz_team_id' and attrib !='_state' and attrib !='id':
                    row.append(value)
            j=j+1

        item.number_members = j-1
        item.save()
        writer.writerow(row)
    return response



def assign_ques(request,team):

    queslist = random.sample(range(1, 7), 3)

    for quesno in queslist:
        ques = Question.objects.get(pk = quesno)
        team.allquestions.add(ques)
        team.save()

def quiz_login(request):
    
    
    if 'username' in request.POST.keys():  
          
        username = request.POST['username']
        password = request.POST['password']

        try:
            team = Quiz_Team.objects.get(teamid = username)
            # if team.leader_email[-12:] == "iitbhu.ac.in" or team.leader_email[-11:] == "itbhu.ac.in":
            #     error
            currUser = authenticate(request, username=username, password=password)
            login(request,currUser)
            return redirect("/questionnaire/quiz_portal")


        except:
            return render(request,'questionnaire/login.html',{'error':"Team Id and Password do not match"})
    else:

        if request.user.is_authenticated == True:
            try:
                team = Quiz_Team.objects.get(teamid = request.user.username)
                #return redirect("/questionnaire/quiz_portal")
            except:
                return render(request,'questionnaire/login.html')
    
        return render(request,'questionnaire/login.html')

def quiz_portal(request):

    try:
            #team = Quiz_Team.objects.get(teamid = request.user.username)
        #if request.user.is_staff == True or team.leader_email=="it@iit.com":
            team = Quiz_Team.objects.get(teamid = request.user.username)
            curr_time=datetime.datetime.now()
            curr_hour = curr_time.hour
            curr_minute = curr_time.minute
            start_hour = 19
            start_minute = 10
            end_hour = 20
            end_minute = 15

            start_timer = max(0,start_hour*60 -curr_hour*60 + start_minute-curr_minute)*60000
            end_timer = max(0,end_hour*60 -curr_hour*60 + end_minute-curr_minute)*60000
            if team.teamid == "TST1":
                start_timer = 0
    #         start_timer = int(min(0,start_hour*60 -curr_hour*60 + start_minute-curr_hour)*60000)
    #         end_timer = int(min(0,end_hour*60 -curr_hour*60 + end_minute-curr_hour)*60000) 
    # >>>>>>> 6f973ea23636f91142b301509639d4059d065942
            allquestions = team.allquestions.all()
            questionList = []
            useranswers = team.allanswers.all()
            if team.not_submitted == False:
                end_timer = 0
            for question in allquestions:
                currans = "0"
                for answer in useranswers:
                    if str(answer.ques_id) == str(question.id):
                        currans = str(answer.ans)

                questionList.append({'id':question.id,'question':question.ques,'options':[question.option1,question.option2,question.option3,question.option4],'ans':currans})
            return render(request,'questionnaire/main.html',{'questionList':questionList,'start_timer':start_timer,'end_timer':end_timer})
        # else:
        #     return Http404
    except:
        return redirect('/questionnaire/login')
            

def anssubmit_ajax(request):

    team = Quiz_Team.objects.get(teamid = request.user.username)
    curr_time=datetime.datetime.now()
    curr_hour = curr_time.hour
    curr_minute = curr_time.minute
    start_hour = 19
    start_minute = 10
    end_hour = 20
    end_minute = 15
    end_timer = max(0,end_hour*60 -curr_hour*60 + end_minute-curr_minute)*60000
    if team.not_submitted == False:
        end_timer = 0
    if end_timer == 0:
        return JsonResponse({'error':True})

    
    data = json.loads(request.body)
    #return JsonResponse({'error':data})
    qid = data['q_id']
    if str(qid) == str(-1):
        team.not_submitted = False
        team.save()
        return JsonResponse({'error':True})

    old_ans = False
    allanswers = team.allanswers.all()
    for ans in allanswers:
        if str(ans.ques_id) == qid:
            ans.ans = data['q_ans']
            ans.save()
            old_ans = True
    if old_ans == False:
        new_Ans = Ans_chosen()
        new_Ans.ques_id = qid
        new_Ans.ans = data['q_ans']
        new_Ans.save()
        team.allanswers.add(new_Ans)
        team.save()

    return JsonResponse({'error':qid,'end_timer':end_timer})


def get_answers(request):
    if not request.user.is_staff:
        return HttpResponse("Permission Denied")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="questionnaire_teams.csv"'
    allTeams = Quiz_Team.objects.all()
    writer = csv.writer(response)
    row = ['S No.']
    i=0
    for item in allTeams:
        if item.team_name[:3]!="TST":
            if i==0:
                for attrib,value in item.__dict__.items():
                    if attrib !='_state' and attrib !='id' and attrib !='allanswers' and attrib !='allquestions':
                        row.append(attrib.title())
                row.append("college")

                for k in range(1,11):
                    row.append("answer"+str(k))
                members = item.team_member_set.all()

                j=1
                for member in members:
                    if j==1:
                        for attrib,value in member.__dict__.items():
                            if attrib != 'quiz_team_id' and attrib !='_state' and attrib !='id':
                                row.append(attrib+str(j))
                        for attrib,value in member.__dict__.items():
                            if attrib != 'quiz_team_id' and attrib !='_state' and attrib !='id':
                                row.append(attrib+str(j+1))
                    j=j+1
                writer.writerow(row)
                
                
                j=1
                
            i=i+1
            row = [i]

            for attrib,value in item.__dict__.items():
                if attrib !='_state' and attrib !='id':
                    row.append(value)
            college = ""
            members = item.team_member_set.all()
            for member in members:
                    college = member.college
            row.append(college)
            r = []
            for k in range(20):
                r.append(0)
            allanswers = item.allanswers.all()
            c=0
            for ans in allanswers:
                c=c+1
                if ans.ans!=0:
                    r[int(ans.ques_id)-1] = ans.ans
            for k in range(10):
                row.append(r[k])
            members = item.team_member_set.all()
            
            for member in members:
                for attrib,value in member.__dict__.items():
                    if attrib != 'quiz_team_id' and attrib !='_state' and attrib !='id':
                        row.append(value)
            if c>0:
                item.score=1
                item.save()
                writer.writerow(row)
            else:
                i=i-1

    return response
    # allteams = Quiz_Team.objects.all()
    # num_teams = 0
    # for team in allteams:
    #     anss = team.allanswers.all()
    #     count = 0
    #     for ans in anss:
            
    #     if count > 0 and team.teamid[:3]!='TST':# and team.leader_email[-11:]!="itbhu.ac.in" and team.leader_email[-12:]!="iitbhu.ac.in":
    #         num_teams=num_teams+1



# for i in range(40):
#     new_team = Quiz_Team()
#     new_team.team_name="test"+str(i)
#     new_team.leader_email="it@iit.com"
#     new_team.password="password"
#     new_team.number_members=1
#     new_team.teamid="TST"+str(i)
#     new_team.save()
#     currUser = User.objects.create_user(username=new_team.teamid, email=new_team.leader_email, password=new_team.password)
#     currUser.save()
#     for j in range(11,21):
#         ques = Question.objects.get(pk=j)
#         new_team.allquestions.add(ques)
#         new_team.save()
# from django.http import Http404
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.template import loader
# from django.views.generic import TemplateView
# from questionnaire.models import *
# from user.models import *
# from django.contrib.auth.models import User, UserManager
# from django.contrib.auth import authenticate,login,logout
# from django.http import JsonResponse
# from django.shortcuts import redirect
# from django.utils.crypto import get_random_string
# from django.core.mail import send_mail, get_connection
# import csv
# import random
# import datetime
# import json

# admin_email = ['Admin@shilpiitbhu.org','events@shilpiitbhu.org','questionnaire@shilpiitbhu.org','eventsteam@shilpiitbhu.org']
# admin_password = ['shilp2018','eventsshilp','teamstark','teamstark']
# allteams = Quiz_Team.objects.all()
# my_host = 'smtp.zoho.com'
# my_port = 587
# my_use_tls = True

# for team in allteams:
#     title = 'Shilp : Reminder for Questionnaire'
#     content1 = "Hello Team " + team.team_name + ",\n\nGreetings from Team Shilp!\n\nWe are happy to inform you that Slot 2 of Questionnaire will be live today (24/09/18) from 7pm to 8pm so if you missed the contest yesterday you can take part today. You are expected to login before 7pm for convenience. Go to shilpiitbhu.org/questionnaire/login and login with following details."
#     content2 = "\nYour Team Name is :" + team.team_name + "\nYour TeamId is : "+ team.teamid+"\n"
#     content3 = "\nYour Password is  : "+ team.password+"\n"
#     content4 = "\n\nFeel free to explore our website for further details."
#     content5 = "\n\nIn case you have not registered for the event or have any queries, feel free to contact us at admin@shilpiitbhu.org, we'll be happy to help you!\n"
#     content6 = "\n\nBest Wishes,\nTeam Shilp\nIIT(BHU) Varanasi."
#     content = content1 + content2 + content3 + content4 + content5 + content6
        
#     for i in range(4):
#         try:
#             connection1 = get_connection(host=my_host,port=my_port,username=admin_email[i],password=admin_password[i],use_tls=my_use_tls) 
#             send_mail(title, content, admin_email[i] ,[team.leader_email], fail_silently=False,connection = connection1)                        
#             break
#         except:
#             c=0



# from django.http import Http404
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.template import loader
# from django.views.generic import TemplateView
# from questionnaire.models import *
# from user.models import *
# from django.contrib.auth.models import User, UserManager
# from django.contrib.auth import authenticate,login,logout
# from django.http import JsonResponse
# from django.shortcuts import redirect
# from django.utils.crypto import get_random_string
# from django.core.mail import send_mail, get_connection
# import csv
# import random
# import datetime
# import json

# allteams = Quiz_Team.objects.all()
# num_teams = 0
# for team in allteams:
#     anss = team.allanswers.all()
#     count = 0
#     for ans in anss:
#         count=count+1
#     if count > 0 and team.teamid[:3]!='TST':# and team.leader_email[-11:]!="itbhu.ac.in" and team.leader_email[-12:]!="iitbhu.ac.in":
#         num_teams=num_teams+1
        
# # print(num_teams)
          
