from django.conf.urls import patterns, include, url
from students import views
#from django.views.generic import ListView


urlpatterns = patterns('',
	#url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^bulletin$', views.BulletinView.as_view(), name='bulletin'),
	url(r'^profile$', views.ProfileView.as_view(), name='profile'),
	url(r'^shelf$', views.ShelfView.as_view(), name='shelf'),
	url(r'^classroom$', views.ClassroomView.as_view(), name='classroom'),
)