from django.conf.urls import patterns, url
from iips_site import views
from django.views.generic import ListView


urlpatterns = patterns('',
     url(r'^$', views.HomeView.as_view(), name='home'),
     url(r'^admission/$', views.AdmissionView.as_view(), name='admission'),
     url(r'^admission/(?P<pk>\d+)/$', views.AdmissionDetailView.as_view(), name='admissiondetail'),
     url(r'^program/$', views.ProgramView.as_view(), name='program'),
     url(r'^program/(?P<pk>\d+)/$', views.ProgramDetailView.as_view(), name='programdetail'),
     url(r'^news/$', views.NewsView.as_view(), name='news'),
     url(r'^notification/$', views.NotificationView.as_view(), name='notifications'),
     url(r'^syllabus/$', views.SyllabusView.as_view(), name='syllabus'),
     #url(r'^syllabus/(?P<pk>\d+)/$', views.SyllabusSemesterView.as_view(), name='syllabusdetail'),
     #url(r'^syllabus/([^/]+)/(?P<pk>\d+)/$', views.SyllabusSubjectView.as_view(), name='syllabussubject'),
     url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
     #url(r'^contact/$', views.contact(), name='contact'),
     url(r'^staff_info/$', views.StaffInfoView.as_view(), name='staff_info'),
     url(r'^faculty_info/$', views.FacultyInfoView.as_view(), name='faculty_info'),
     url(r'^development_center/$', views.HomeView.as_view(), name='development_center'),
     url(r'^research_center/$', views.HomeView.as_view(), name='research_center'),
     url(r'^publication/$', views.HomeView.as_view(), name='publications'),
     url(r'^placement/$', views.PlacementView.as_view(), name='placement'),
     url(r'^placement/list$', views.PlacementListView.as_view(), name='placementlist'),
     url(r'^placement/complanies$', views.PlacementCompanyView.as_view(), name='placementcompany'),
     url(r'^tab/$',views.tabs),


)