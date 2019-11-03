from django.shortcuts import render
from .forms import CaForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import csv
from django.core.mail import send_mail

admin_email = ['Admin@shilpiitbhu.org','events@shilpiitbhu.org','eventsteam@shilpiitbhu.org']
admin_password = ['shilp2018','eventsshilp','teamstark']

checkforreg = False

def index(request):
    global checkforreg
    checkreg = checkforreg
    checkforreg = False
    return render(request,"ca/index.html",{'checkreg':checkreg})


def imgnameChange(str2):
    i=0
    #loop
    while i < len(str2):

        if str2[i] == ' ':# checking if space and replacing it with _
            str1 = str2[:i]+'_'+str2[i+1:]
            str2 = str1
        i=i+1
    return str2.upper()


def register(request):
    if 'fname' not in request.POST.keys():
        return render(request, 'ca/login_n_reg.html')
    else:

        try:
            caObject = Ca()
            caObject.name = request.POST['fname']
            a = str(caObject.name)
            caObject.email = request.POST['email']
            b = str(caObject.email)
            caObject.phone = request.POST['phone']
            c = str(caObject.phone)
            caObject.gender = request.POST['gender']
            d = str(caObject.gender)
            caObject.college = request.POST['college']
            e = str(caObject.college)
            caObject.year = request.POST['year']
            f = str(caObject.year)
            caObject.comment = request.POST['comment']
            g = str(caObject.comment)
            caObject.points = 0
            #img = request.FILES['img']  # getting file
            #fs = FileSystemStorage()  # getting reference to storage
            #img.name = imgnameChange(img.name)  # getting name of file
            #filename = fs.save(img.name, img)
            #caObject.path = "image/" + filename 
            #caObject.image.name = filename
            #caObject.save()
            caObject.save()
            message_body1 = "Hello " + caObject.name + ",\n\nGreetings from Team Shilp!\n\nWe are happy to inform you that "
            message_body2 = "you have successfully registered for Campus Ambassador of Shilp'18. There are special perks for the best Campus Ambassadors."
            message_body3 = "\n\nYou'll soon be contacted for the telephonic interview process. In case you have any queries feel free to contact us, we will be more than happy to help you!\n\n"
            message_body4 = "Best Wishes,\n\nTeam Shilp\nIIT(BHU) Varanasi.\n"
            message_body = message_body1 + message_body2 +message_body3 + message_body4
            message_subject = "Registration for CA at Shilp'18 Successful!"
            #sending mail to user
            send_mail(message_subject, message_body, 'admin@shilpiitbhu.org',
                [caObject.email], fail_silently=True)
            subject = "New Registration for CA"
            m1 = "Hi, a new user has registered for CA at Shilp'18 with the following details:\n\n"
            m2 = "Name\t\t: "+a+"\nEmail\t\t: "+b+"\nPhone\t\t: "+c+"\nGender\t\t: "+d+"\nCollege\t\t: "+e+"\nYear\t\t: "+f
            m3 = "\nComment\t\t: "+g+ "\n\nRegards,\nShilp Backend.\n"
            #sending mail to team
            send_mail(subject, m1+m2+m3, 'admin@shilpiitbhu.org',
                ['shilpshobhit2018@gmail.com', 'ruinedwrath@gmail.com'], fail_silently=True)
            global checkforreg
            checkforreg = True
            return redirect('/ca')
            #return render(request, 'ca/index.html')
        except:
            return render(request, 'ca/login_n_reg.html',{'error': "Please Enter All Details Correctly"})
        

def postMessage(request):
    try:
        messageObject = Message()
        messageObject.name = request.POST['name']
        a = messageObject.name
        messageObject.email = request.POST['email']
        b = messageObject.email
        messageObject.subject = request.POST['subject']
        c = messageObject.subject
        messageObject.message = request.POST['message']
        d = messageObject.message
        messageObject.save()
        subject = "New Message from Shilp website"
        body = "Name\t\t: " + a + "\nEmail\t\t: " + b + "\nSubject\t\t: "+ c+ "\n\n" + d +"\n\n\nRegards,\nShilp Backend\n"
        #sending mail to team
        for i in range(4):
            try:
                connection1 = get_connection(host=my_host, 
                    port=my_port, 
                    username=admin_email[i], 
                    password=admin_password[i], 
                    use_tls=my_use_tls) 
                send_mail(title, subject, body, 'shilp@iitbhu.ac.in',['shilpshobhit2018@gmail.com'], fail_silently=False,connection = connection1)                        
                break
            
            except:
                c=0
        
        return JsonResponse({'msg':'OK'})
    except:
        return JsonResponse({'msg':'Servers Are Busy Right Now'})





def leaderboard(request):
    allCa = Ca.objects.all();
    leaderList = []
    for ca in allCa:
        leaderList.append(ca)

    return render(request,'ca/leaderboard.html',{'leaderList':leaderList})


def download_csv(request):
    if not request.user.is_staff:
        return HttpResponse("Permission Denied")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    allCaObjects = Ca.objects.all()
    writer = csv.writer(response)
    row = ['S No.']
    i=0
    for item in allCaObjects:
        if i==0:
            for attrib,value in item.__dict__.items():
                if attrib != 'image' and attrib !='_state' and attrib !='id':
                    row.append(attrib)
            writer.writerow(row)
        i=i+1
        row = [i]
        for attrib,value in item.__dict__.items():
            if attrib != 'image' and attrib != '_state' and attrib !='id':
                row.append(value)
        writer.writerow(row)
    return response

def downloadMessage(request):
    if not request.user.is_staff:
        return HttpResponse("Permission Denied")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    allCaObjects = Message.objects.all()
    writer = csv.writer(response)
    row = ['S No.']
    i=0
    for item in allCaObjects:
        if i==0:
            for attrib,value in item.__dict__.items():
                if attrib != 'image' and attrib !='_state' and attrib !='id':
                    row.append(attrib)
            writer.writerow(row)
        i=i+1
        row = [i]
        for attrib,value in item.__dict__.items():
            if attrib != 'image' and attrib != '_state' and attrib !='id':
                row.append(value)
        writer.writerow(row)
    return response
    
def post_detail(request, pk):
    ca = get_object_or_404(ca, pk=pk)
    return render(request, 'ca/post_detail.html', {'ca': ca})
def post_new(request):
    return render(request, 'ca/login_n_reg.html')
    if request.method == "CA":
        form = CaForm(request.CA)
        if form.is_valid():
            ca = form.save(commit=False)
            ca.name = request.user
            ca.save()
            return redirect('post_detail', pk=ca.pk)
    else:
        form = CaForm()
    return render(request, 'ca/post_edit.html', {'form': form})
def post_edit(request, pk):
    ca = get_object_or_404(Ca, pk=pk)
    if request.method == "CA":
        form = CaForm(request.CA, instance=ca)
        if form.is_valid():
            ca = form.save(commit=False)
            ca.name = request.user
            ca.save()
            return redirect('post_detail', pk=ca.pk)
    else:
        form = CaForm(instance=ca)
    return render(request, 'ca/post_edit.html', {'form': form})
