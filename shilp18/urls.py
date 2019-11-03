from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^shilpadmin/', admin.site.urls),
    url(r'^ca/', include('ca.urls')),
    url(r'^user/', include('user.urls')),
    url(r'', include('homepage.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^questionnaire/', include('questionnaire.urls'))

]
