from django.conf.urls import patterns, url
from iips_site import views


urlpatterns = patterns('',
     url(r'^$', views.IndexView.as_view(), name='index'),
     url(r'^gallary/$', views.GallaryView.as_view(), name='gallary'),
     #url(r'^programs/$', views.ProgramsView.as_view(), name='programs')
)