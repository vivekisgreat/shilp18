from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'questionnaire'
urlpatterns = [
    url(r'^registration$', views.registration, name='registration'),
    url(r'^download_questionnaire$', views.download_questionnaire, name = 'download_questionnaire'),
    url(r'^quiz_portal$', views.quiz_portal, name = 'quiz_portal'),
	url(r'^login$', views.quiz_login, name = 'login'),
	url(r'^anssubmit_ajax$', views.anssubmit_ajax, name = 'anssubmit_ajax'),
	url(r'^get_ans$', views.get_answers, name = 'get_answers'),
    
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

