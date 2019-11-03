from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'dashboard'
urlpatterns = [
    url(r'^event_reg/$', views.event_reg, name='event_reg'),
    url(r'^RegPlan/$', views.RegPlan, name='RegPlan'),
    url(r'^team_reg/$', views.team_reg, name='team_reg'),
    url(r'^regplanajax/$', views.regplanajax, name = 'regplan_ajax'),
    url(r'^txformajax/$', views.txformajax, name = 'txformajax'),
    url(r'^team_regajax/$', views.team_regajax, name = 'team_regajax'),
    url(r'^$', views.profile, name = 'profile'),
    url(r'^help/$', views.help, name = 'help'),
    url(r'^payment/$', views.payment, name = 'payment')

]
'''
    url(r'^ca/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^ca/new/$', views.post_new, name='post_new'),
    url(r'^ca/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
<<<<<<< HEAD
'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


