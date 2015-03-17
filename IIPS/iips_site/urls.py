from django.conf.urls import patterns, url
from iips_site import views
from django.views.generic import ListView


urlpatterns = patterns('',
     url(r'^$', views.IndexView.as_view(), name='index'),
)