from django.conf.urls import patterns, include, url
from events import views
from django.views.generic import ListView
from .models import *


urlpatterns = patterns('',
	url(r'^$', views.EventView.as_view(), name='event'),
	url(r'^(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='eventdetail'),
	#url(r'^register/(?P<pk>\d+)/$', views.TeamRegisterationView.as_view(), name='teamregisteration'),#kwargs=dict('event_id'=1),
	#url(r'^register/(?P<pk>\d+)//$', views.TeamRegistrationView2.as_view(), name='teamregisteration2'),
	url(r'^oc/(?P<pk>\d+)/$',views.OCView.as_view(), name='ocdetail'),
	url(r'^event/(?P<pk>\d+)/$',views.SubEventView.as_view(), name='subevent'),
	url(r'^register/team_member/(?P<pk>\d+)/$', views.TeamRegisterationView.as_view(), name='teamregisteration'),
    #url(r'^team_created$', views.teamCreatedView, name='team-created'),
)	