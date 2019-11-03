from django.conf.urls import url

from . import views



app_name = 'user'



urlpatterns = [



    url(r'^register/$',views.UserRegister.as_view(), name = "registration"),
    url(r'^$',views.dashboard,name = "dashboard"),
    url(r'^dashboard/$',views.dashboard,name = "dashboard"),


]
