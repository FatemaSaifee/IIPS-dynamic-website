from django.conf.urls import patterns, url
from data_entry import views


urlpatterns = patterns('',
	url(r'^temp_table/$', 'data_entry.views.temp_table',name='home'),
	url(r'^$', 'data_entry.views.login'),   #displays login.html
	url(r'^accounts/auth/$', 'data_entry.views.auth_view'),    #authorize login
	url(r'^accounts/loggedin', 'data_entry.loggedin_view'),
	url(r'^accounts/invalid$', 'data_entry.invalid_view'),
)