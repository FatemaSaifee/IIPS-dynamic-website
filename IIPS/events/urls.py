from django.conf.urls import patterns, include, url
from events import views
from django.views.generic import ListView


urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='event'),
	
    #url(r'^admission/$', views.AdmissionView.as_view(), name='admission'),
)