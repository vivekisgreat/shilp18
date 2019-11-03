from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login
from .models import User,Profiles
from .forms import UserForm
from django.views.generic import View
# Create your views here.
class UserRegister(View):
    form_class = UserForm
    template_name = 'homepage/login.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            
            user = form.save(commit = False)
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user.set_password(password)
            user.save()
            profile = user.userprofile
            profile.user = user
            profile.name = form.cleaned_data.get('name')
            profile.mobile_no = form.cleaned_data.get('mobile_no')
            profile.college_name = form.cleaned_data.get('college_name')
            profile.year = form.cleaned_data.get('year')
            profile.residential_address = form.cleaned_data.get('residential_address')
            profile.save()
            login(request, user)

            if user is not None:
                if user.is_active:
                    return redirect('/user/dashboard')
        return render(request, self.template_name, {'form':form})


def dashboard(request):
    currUser = request.user
    return HttpResponse(request.user.username)






