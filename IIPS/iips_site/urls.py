from django.conf.urls import patterns, url
from iips_site import views
from django.views.generic import ListView


urlpatterns = patterns('',
     url(r'^$', views.IndexView.as_view(), name='index'),
     url(r'^home/$', views.HomeView.as_view(), name='home'),
     #url(r'^exampleanjee/$', views.exampleanjeeView.as_view(), name='exampleanjee'),
     url(r'^exampleanjee/$', views.HomeView.as_view(), name='exampleanjee'),
     url(r'^admission/$', views.HomeView.as_view(), name='admission'),
     url(r'^program/$', views.HomeView.as_view(), name='programs'),
     url(r'^news/$', views.HomeView.as_view(), name='news'),
     url(r'^notification/$', views.HomeView.as_view(), name='notifications'),
     url(r'^syllabus/$', views.HomeView.as_view(), name='syllabus'),
     url(r'^calendar/$', views.HomeView.as_view(), name='calendar'),
     url(r'^contact/$', views.HomeView.as_view(), name='contact'),
     url(r'^staff_info/$', views.HomeView.as_view(), name='staff_info'),
     url(r'^faculty_info/$', views.HomeView.as_view(), name='faculty_info'),
     url(r'^development_center/$', views.HomeView.as_view(), name='development_center'),
     url(r'^research_center/$', views.HomeView.as_view(), name='research_center'),
     url(r'^publication/$', views.HomeView.as_view(), name='publications'),
     url(r'^placement/$', views.HomeView.as_view(), name='placements'),


)