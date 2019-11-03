from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'ca'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.register, name='register'),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    url(r'^postmessage/$', views.postMessage, name='postmessage'),
    url(r'^downloadcsv/$', views.download_csv, name='downloadcsv'),
    url(r'^downloadmsg/$', views.downloadMessage, name='downloadmsg'),





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

