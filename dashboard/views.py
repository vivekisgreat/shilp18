from django.shortcuts import render
from user.models import *
from django.contrib.auth.models import User, UserManager
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.mail import send_mail

# Create your views here.
#plans = {'0x0':'Workshop Accomodation (1 day)','120':'Workshop Accomodation (2 day) ','130':'Workshop Accomodation (3 day)','100':'Classic','110':'Classic+','200':'Silver','210':'Silver+','300':'Gold','310':'Gold+','301':'Platinum','311':'Platinum+'}
#money = {'0x0':'300','120':'600','130':'900','010':'500','100':'300','110':'600','200':'400','210':'700','300':'500','310':'800','301':'750','311':'1000'}
plans = {'100':'Classic','200':'Silver','300':'Gold','301':'Platinum'}
money = {'010':'500','100':'300','110':'600','200':'400','210':'700','300':'500','310':'800','301':'750','311':'1000'}
#dict_event = {'questionare':'','':'','':'', '': '', '': '', '': '', '': '', '': '', '': '', '':''}
def event_reg(request):
	try:
		currUser = request.user
		userProfile = currUser.profiles
		cntevent = 0
		error = False
		locked = userProfile.events_locked
		events = []
		for attr, value in userProfile.__dict__.items():
							
			if attr[:6]=="event_" and value == True:
				events.append(attr[6:])
		if locked == False:
			for attr, value in userProfile.__dict__.items():
				#request.POST['abc']
				if attr[6:] in request.POST.keys():
					userProfile.__dict__[attr] = True
					
					if userProfile.payment_plan == 'Freshers':
						userProfile.events_locked=True

					if cntevent > userProfile.num_events and cntevent>0 :
						break
					cntevent=cntevent+1

				elif attr[:6]=="event_":
					userProfile.__dict__[attr] = False


		if cntevent > userProfile.num_events:
			error = True
		elif cntevent >0:
			events = []
			for attr, value in userProfile.__dict__.items():
								
				if attr[:6]=="event_" and value == True:
					events.append(attr[6:])
			userProfile.save()
		return render(request, 'dashboard/event_reg.html',{'User':currUser,'Profile':userProfile,'events':events,'error':error})

	except:
		return redirect('/login')


def RegPlan(request):
	try:
		currUser = request.user
		userProfile = currUser.profiles
		events = []
		for attr, value in userProfile.__dict__.items():
							
			if attr[:5]=="event" and value == True:
				events.append(attr[6:].capitalize())
		packsList = []
		for key in plans:
			packsList.append((key,plans[key]))

		return render(request, 'dashboard/RegPlan.html',{'User':currUser,'Profile':userProfile,'events':events,'plans':packsList})
		
	except:
		return redirect('/login')

def team_reg(request):


	try:
		currUser = request.user
		userProfile = currUser.profiles
		events = []
		for attr, value in userProfile.__dict__.items():
							
			if attr[:6]=="event_" and value == True:
				events.append(attr[6:].title().replace('_',' '))
		dict_participants = {'Questionnaire':2,'Nirman':4,'Icreate':2,'Delta':2,'Mudmarine':6,'This Way That Way':4, 'Idp':3, 'Enviro': 5 , 'Colloquium': 3}
		return render(request, 'dashboard/team_reg.html',{'User':currUser,'Profile':userProfile,'events':events,'participants':dict_participants})


	except:
		return redirect('/login')

def regplanajax(request):
	global plans
	plan = request.POST['selectLg']
	currUser = request.user
	userProfile = currUser.profiles
	userProfile.payment_plan = plans[plan]
	if userProfile.txid_submitted == True and userProfile.payment_plan != 'Freshers':
		return JsonResponse({'error':True})
	userProfile.plan_locked = True
	if plan[1] == '0':
		userProfile.accomodation = False
	else:
		userProfile.accomodation = True

	if plan[2] == '0':

		userProfile.tshirt = False
	else:
		userProfile.tshirt = True
	
	userProfile.num_events = int(plan[0])
	userProfile.money = money[plan]
	if userProfile.num_events == 3:
		userProfile.num_events = 8
	for attr, value in userProfile.__dict__.items():
		if attr[:5] == 'event':
			userProfile.__dict__[attr]=False
	userProfile.save()

	return JsonResponse({'chosenPlan':plans[plan],'money':money[plan]})

def txformajax(request):
	txid = request.POST['txn-id']
	currUser = request.user
	profile = currUser.profiles
	profile.events_locked=True
	profile.txid_submitted= True
	profile.txid = txid
	profile.save()
	title = "New Payment Id submitted"
	content = "Hello, A new user has entered his payment details\n\n The details are as below:\n\n"
	content1 = "\nEmail id : "+ currUser.email
	content2 = "\nName : " + profile.name
	content3 = "\nShilpid : " + profile.shilpid
	content4 = "\nMobile no : "+ profile.mobile_no
	content5 = "\nCollege :" + profile.college_name
	content6 = "\nClass and year : " + profile.course + " ,year "+profile.year
	content7 = "\nTransaction id: "+ txid
	content6 = content6+content7
	admin_email1 = 'shilpshobhit2018@gmail.com'
	admin_email2 = 'ruinedwrath@gmail.com'
	content = content+content1 + content2 + content3 + content4 + content5 + content6
	send_mail(title, content, 'admin@shilpiitbhu.org',[admin_email1], fail_silently=False)
	#send_mail(title, content, 'admin@shilpiitbhu.org',[admin_email2], fail_silently=False)
	return JsonResponse({'txid':txid,'payment_verified':False,'txid_submitted':True})


def team_regajax(request):
	dict_participants = {'Questionnaire':2,'Nirman':4,'Icreate':2,'Delta':2,'Mudmarine':6,'This Way That Way':4, 'Idp':3, 'Enviro': 5 , 'Colloquium': 3}
	currUser = request.user
	userProfile = currUser.profiles
	event = request.POST['event']
	eventname = event.lower().replace(' ','_')
	team_name = request.POST['team-name']
	error = False
	members = []
	memberError = []
	#return JsonResponse({'members':members,'memberError':memberError})#, 'participants': dict_participants[event],'allmembers':allmembers})
	allmembers = []
	content3 = "Team Name : " + team_name +"\nEvent : " + event + "\n"
	counter = 1
	allTeams = Team.objects.filter(event = event)
	for i in range(1, dict_participants[event]+1):
		if request.POST['member'+str(i)]!="":

			memberid = request.POST['member'+str(i)]
			allmembers.append(memberid)
			try:
				profile = Profiles.objects.get(shilpid = memberid)
				if profile.payment_verified == False or profile.__dict__['event_'+eventname]==False or profile.__dict__['team_'+eventname]==True:
					error = True
					memberError.append(memberid)
				else:
					
					members.append(memberid)
					content3 = content3 + str(counter) + ". "+profile.name
					if counter == 1:
						content3 = content3 + " (Leader)"
					content3 = content3 + "\n"
					counter = counter + 1

			except:
				memberError.append(memberid)
				error = True


	if error == False:
		
		newTeam = Team()
		newTeam.event = event
		newTeam.team_name = team_name
		for i in range(6):
			if i == len(members):
				break
			newTeam.__dict__["member"+str(i+1)] = members[i]
			title = "Team Registration for "+ event
			#content_url = "shilpiyakepapa.herokuapp.com/confirmation/" + p.shilpid + "/" + str(p.confirmation_code)
			p = Profiles.objects.get(shilpid = members[i])
			p.__dict__['team_'+eventname]=True
			p.save()
			user = p.user
			content1 = "Hello " + p.name + ",\n\nGreetings from Team Shilp!\n\nWe are happy to inform you that your team is successfully registered for event '" + event+"'"
			content2 = "\nDetails :-\n"
			content4 = "\n\nBest of Luck"
			content5 = "\n\nIn case you have any queries, feel free to reply to this mail, we'll be happy to help you!\n"
			content6 = "\n\nBest Wishes,\nTeam Shilp\nIIT(BHU) Varanasi."

			content = content1 + content2 + content3 + content4 + content5 + content6
			send_mail(title, content, 'admin@shilpiitbhu.org', [user.email], fail_silently=True)
		newTeam.save()

	return JsonResponse({'members':members,'memberError':memberError, 'participants': dict_participants[event],'allmembers':allmembers})
	return render(request, 'dashboard/team_reg.html',{'User':currUser,'Profile':userProfile,'members':members,'memberError':memberError})
	

def profile(request):
	try:
		currUser = request.user
		userProfile = currUser.profiles
		shilpid = userProfile.shilpid
		teams = Team.objects.all()
		teamList = []
		for team in teams:
			for attr, value in team.__dict__.items():
				if attr[:6]=="member" and value == shilpid:
					if attr =="member1":
						teamList.append((team.event+"(Leader)",team.team_name))
					else:
						teamList.append((team.event+"(Member)",team.team_name))

					
		return render(request,'dashboard/Profile.html',{'Profile':userProfile,'teams':teamList})

	except:
		return redirect('/login')

def help(request):
	try:
		currUser = request.user
		userProfile = currUser.profiles
		return render(request,'dashboard/Help.html')
	except:
		return redirect('/login')

def payment(request):
	try:
		currUser = request.user
		userProfile = currUser.profiles
		return render(request,'dashboard/Payment.html',{'Profile':userProfile})
	except:
		return redirect('/login')

