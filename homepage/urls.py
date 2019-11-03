from django.conf.urls import url
from . import views



app_name = 'homepage'
urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^indiv/(?P<event_name>\w+)$', views.indiv, name='indiv'),
   url(r'^login/$', views.sign_in, name='login'),
   url(r'^allevents/$', views.allevents, name='allevents'),
   url(r'^hospi/$', views.hospi, name='hospi'),
   #url(r'^dashboard/$', views.dashboard, name = 'dashboard'),
   url(r'^confirmation/(?P<username>\w+)/(?P<confirmation_code>\w+)/$',views.confirm, name = 'confirmation'),
   url(r'^get_teams/(?P<event>\w+)$',views.get_teams, name = 'get_teams'),

   url(r'^team/$', views.team, name='team'),
   url(r'^logout/$', views.signout, name='logout'),
   url(r'^download_users/$', views.download_users, name='download_users'),
   url(r'^download_quiz/$', views.download_quiz, name='download_quiz'),
   url(r'^download_hospi/$', views.download_hospi, name='download_hospi'),



   #url(r'^login/$', views.login, name='login')
]
