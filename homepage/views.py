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
from django.core.mail import send_mail
from questionnaire.models import *
import csv

admin_email = ['ruinedwrath@gmail.com','events@shilpiitbhu.org','eventsteam@shilpiitbhu.org']
admin_password = ['shilp2018','eventsshilp','teamstark']

def index(request):
	context = {}
	if not request.user.is_authenticated:
		context['if_auth'] = False
	else :
		context['if_auth'] = True

	return render(request,'homepage/index.html',context)

def indiv(request,event_name):

	
	if len(event_name) > 3:
		event_name = event_name.title().replace('_',' ')
	
	if event_name == 'Icreate':
		event_name = 'iCreate'

	if event_name == 'Automobile And Ic Engine Design':
		event_name = 'Automobile and IC Engine Design'

	if event_name == 'Robotics And Iot':
		event_name = 'Robotics and IOT'
	currEvent = Event.objects.filter(name = event_name)
	for event in currEvent:
		currEvent = event
		eventDetails = event.detail_set.all()
		detailsList = []
		for details in eventDetails:
			detailsList.append(details.detail)

	context = {'detailsList':detailsList,'event':currEvent}
	if not request.user.is_authenticated:
		context['if_auth'] = False
	else :
		context['if_auth'] = True
	return render(request, 'homepage/individual-event.html',context)

def sign_in(request):

	if request.user.is_authenticated:
		try:
			currUser = request.user
			userProfile = currUser.profiles
			return redirect("/dashboard")
		except:
			logout(request)
			return render(request,'homepage/login.html',{'error':"You are trying to login with the Questionnaire Portal Team ID. For Round 2, both members need to indivdually sign up again on the website."})

	#request.POST['dob']	
	if 'dob' in request.POST.keys():
		return sign_up(request)

	if 'username' in request.POST.keys():
		try:
			username = request.POST['username']
			password = request.POST['password']
			currUser = authenticate(request, username=username, password=password)
			login(request,currUser)
			return redirect('/dashboard')				
		except:		
			return render(request,'homepage/login.html',{'error':"Username and Password do not match Or your account is not verified"})
	
	return render(request, 'homepage/login.html')

def sign_up(request):
	

	username = request.POST['username']
	password = request.POST['password']
	email = request.POST['email']
	#return HttpResponse(email)
	try:
		currUser = User.objects.create_user(username=email, email=email, password=password)
		currUser.is_active = False
			
	except:
		return render(request,'homepage/login.html',{'signup_error':"This Email Id is already registered"})
	
	profile = Profiles()
	profile.user = currUser
	profile.name = username
	profile.mobile_no = request.POST['phone']
	profile.college_name = request.POST['college']
	profile.year = request.POST['year']
	profile.course = request.POST['class']
	profile.sex = request.POST['sex']
	profile.dob = request.POST['dob'] +'-'+ request.POST['birthday_month'] +'-'+ request.POST['birthday_year'] 
	profile.residential_address = ""
	profile.confirmation_code = get_random_string(length=32)
	profile.num_events = 0
	profile.payment_plan = "N/A"
	if email[-12:] == "iitbhu.ac.in" or email[-11:] == "itbhu.ac.in":
		profile.num_events = 8
		profile.payment_plan = "Freshers"
		profile.payment_verified = True
		profile.txid_submitted = True
		profile.accomodation = True
		profile.plan_locked = True
		profile.money = 0
	profile.ca_name= request.POST['ca-name']
	profile.save()
	profile.shilpid = "SH100"+str(profile.pk)
	profile.save()
	title = "New Registrant"
	content = "Hello, A new user has signed up\n\n The details are as below:\n\n"
	content1 = "\nEmail id : "+ email
	content2 = "\nName : " + profile.name + "\nPassword: " + password
	content3 = "\nShilpid : " + profile.shilpid
	content4 = "\nMobile no : "+ profile.mobile_no
	content5 = "\nCollege :" + profile.college_name
	content6 = "\nClass and year : " + profile.course + ",\nyear "+profile.year
	content7 = "\nCA name: "+ profile.ca_name
	content6 = content6+content7
	admin_email1 = 'shilpshobhit2018@gmail.com'
	admin_email2 = 'ruinedwrath@gmail.com'
	content = content+content1 + content2 + content3 + content4 + content5 + content6
	send_mail(title, content, 'admin@shilpiitbhu.org',[admin_email1], fail_silently=True)
	#send_mail(title, content, 'admin@shilpiitbhu.org',[admin_email2], fail_silently=False)


	currUser.save()
	try:
		send_registration_confirmation(currUser)
	except:
		return render(request,'homepage/login.html',{'redirect':"Error!!! An email has been sent to your registered email for verification"})

	#login(request,currUser)
	return render(request,'homepage/login.html',{'redirect':"Congratulations!!! An email has been sent to your registered email for verification"})

def send_registration_confirmation(user):
	p = user.profiles
	title = "Registration successful for Shilp 2018"
	content_url = "www.shilpiitbhu.org/confirmation/" + p.shilpid + "/" + str(p.confirmation_code)

	content1 = "Hello " + p.name + ",\n\nGreetings from Team Shilp!\n\nWe are happy to inform you that you have successfully registered for Shilp'18."
	content2 = "\nClick on the following link to verify your account:\n"
	content3 = content_url
	content4 = "\n\nFeel free to explore our website for further details and select the participation package as per your preferences."
	content5 = "\n\nIn case you have any queries, feel free to contact us, we'll be happy to help you!\n"
	content6 = "\n\nBest Wishes,\nTeam Shilp\nIIT(BHU) Varanasi."

	content = content1 + content2 + content3 + content4 + content5 + content6
	send_mail(title, content, 'admin@shilpiitbhu.org', [user.email], fail_silently=True)

def confirm(request, username, confirmation_code):
	
		profile = Profiles.objects.get(shilpid = username)
		user = profile.user
		if profile.confirmation_code == confirmation_code and confirmation_code != '-1':
			profile.confirmation_code = "-1"
			user.is_active = True
			user.save()
			login(request,user)
		return redirect("/dashboard/RegPlan/")
	

def allevents(request):
	context = {}
	if not request.user.is_authenticated:
		context['if_auth'] = False
	else :
		context['if_auth'] = True

	return render(request,'homepage/allevents.html',context)

def hospi(request):
	context = {}
	if not request.user.is_authenticated:
		context['if_auth'] = False
	else :
		context['if_auth'] = True

	return render(request,'homepage/hospitality.html',context)

def dashboard(request):
	return render(request,'homepage/allevents.html')

def team(request):
	context = {}
	if not request.user.is_authenticated:
		context['if_auth'] = False
	else :
		context['if_auth'] = True

	return render(request,'homepage/team.html',context)
	
def signout(request):
	logout(request)
	return redirect('/')

def download_users(request):

	if not request.user.is_staff:
		return HttpResponse("Permission Denied")

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="user_registrations.csv"'
	all_users = Profiles.objects.all()
	writer = csv.writer(response)
	row = ['S No.','email']
	i=0
	for item in all_users:
	    if i==0:
	        for attrib,value in item.__dict__.items():
	            if attrib != 'user_id' and attrib !='_state' and attrib !='id':
	                row.append(attrib.title().replace('_',' '))
	        writer.writerow(row)
	    i=i+1
	    row = [i]
	    row.append(item.user.email)
	    for attrib,value in item.__dict__.items():
	        if attrib != 'user_id' and attrib != '_state' and attrib !='id':
	            row.append(value)
	    writer.writerow(row)
	return response

def download_hospi(request):

	if not request.user.is_staff:
		return HttpResponse("Permission Denied")

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="accod_registrations.csv"'
	all_users = Profiles.objects.all()
	writer = csv.writer(response)
	row = ['S No.']
	i=0

	for item in all_users:
		w_flag=0
		if i==0:
			for attrib,value in item.__dict__.items():
				if attrib == 'name' and attrib == 'mobile_no' and attrib == 'sex' and attrib == 'shilpid'and attrib == 'payment_verified' and attrib == 'name' and attrib == 'payment_plan'  :
					row.append(attrib.title().replace('_',' '))
			row.append('Workshop')
			writer.writerow(row)
		i=i+1
		row = [i]
		for attrib,value in item.__dict__.items():
			if attrib == 'name' and attrib == 'mobile_no' and attrib == 'sex' and attrib == 'shilpid'and attrib == 'payment_verified' and attrib == 'name' and attrib == 'payment_plan' :
				if attrib == 'accomodation':
					if value == True:
						w_flag=1
				if w_flag == 1:
					if attrib == 'payment_plan':
						if value == "Workshop Accomodation (1 day)" or value == "Workshop Accomodation (2 day)" or value == "Workshop Accomodation (3 day)" :
							workshop="Yes"
						else:	
							workshop="No"

					row.append(value)
		if w_flag == 1:
			row.append(workshop)
		writer.writerow(row)
	return response

def download_quiz(request):

	if not request.user.is_staff:
		return HttpResponse("Permission Denied")

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="quiz_registrations.csv"'
	all_teams = Quiz_Team.objects.all()
	writer = csv.writer(response)
	row = ['S No.']
	i=0
	for item in all_teams:
		if i==0:
			for attrib,value in item.__dict__.items():
				if attrib != '_state' and attrib != 'password' :
					row.append(attrib.title().replace('_',' '))
			row.append('Internal')
			writer.writerow(row)
		i=i+1
		row = [i]
		for attrib,value in item.__dict__.items():
			if  attrib != '_state' and attrib != 'password' :
				if attrib == 'leader_email':
					if value[-12:] == "iitbhu.ac.in" or value[-11:] == "itbhu.ac.in":
						internal="Yes"
					else:	
						internal="No"

				row.append(value)
		row.append(internal)
		writer.writerow(row)
	return response

def get_teams(request,event):
	if not request.user.is_staff:
		return HttpResponse("Permission Denied")

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="quiz_registrations.csv"'
	all_teams = Team.objects.all()
	writer = csv.writer(response)
	row = ['S No.']
	i=0
	event = event.title().replace('_',' ')
	for item in all_teams:
		if item.event != event:
			continue
		try:
			leader = Profiles.objects.get(shilpid=item.member1)
			if i==0:
				for attrib,value in item.__dict__.items():
					if attrib != '_state' and attrib != 'password' :
						row.append(attrib.title().replace('_',' '))
				row.append("Leader Name")
				row.append("Leader Email")
				row.append("Leader Contact Number")
				writer.writerow(row)
			i=i+1
			row = [i]
			for attrib,value in item.__dict__.items():
				if  attrib != '_state' and attrib != 'password' :
					if attrib == 'leader_email':
						if value[-12:] == "iitbhu.ac.in" or value[-11:] == "itbhu.ac.in":
							internal="Yes"
						else:	
							internal="No"

					row.append(value)
			row.append(leader.name)
			row.append(leader.user.email)
			row.append(leader.mobile_no)
			writer.writerow(row)
		except:
			c=0
	return response
