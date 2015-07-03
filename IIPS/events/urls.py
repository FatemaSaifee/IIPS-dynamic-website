from django.conf.urls import patterns, include, url
from events import views
from django.views.generic import ListView


urlpatterns = patterns('',
	url(r'^$', views.EventView.as_view(), name='event'),
	url(r'^(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='eventdetail'),
    #url(r'^admission/$', views.AdmissionView.as_view(), name='admission'),
)