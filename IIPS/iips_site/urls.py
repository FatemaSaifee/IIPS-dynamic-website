from django.conf.urls import patterns, include, url
from iips_site import views
from django.views.generic import ListView


urlpatterns = patterns('',
     url(r'^$', views.HomeView.as_view(), name='home'),
     url(r'^admission/$', views.AdmissionView.as_view(), name='admission'),
     url(r'^admission/(?P<pk>\d+)/$', views.AdmissionDetailView.as_view(), name='admissiondetail'),
     url(r'^program/$', views.ProgramView.as_view(), name='program'),
     url(r'^program/(?P<pk>\d+)/$', views.ProgramDetailView.as_view(), name='programdetail'),
     url(r'^news/$', views.NewsView.as_view(), name='news'),
     url(r'^gallary/$',views.GallaryView.as_view(), name='gallary'),
     #url(r'news/(?P<pk>\d+)/$',views.NewsDetail,as_view(), name='newsdetail'),
     url(r'^notification/$', views.NotificationView.as_view(), name='notification'),
     url(r'^syllabus/$', views.SyllabusView.as_view(), name='syllabus'),
     url(r'^syllabus/(?P<pk>\d+)/$', views.SyllabusDetailView.as_view(), name='syllabusdetail'),
     #url(r'^syllabus/([^/]+)/(?P<pk>\d+)/$', views.SyllabusSubjectView.as_view(), name='syllabussubject'),
     url(r'^about-iips/$',views.AboutIIPSView.as_view(), name='aboutiips'),
     url(r'^about-iips/director$',views.AboutIIPSDirectorView.as_view(), name='director'),
     url(r'^about-iips/antiragging$',views.AboutIIPSAntiraggingView.as_view(), name='antiragging'),
     url(r'^about-iips/vision-mission-goal$',views.AboutIIPSVisionView.as_view(), name='visionmissiongoal'),
     url(r'^about-university/$',views.AboutUniversityView.as_view(), name='aboutuniversity'),
     url(r'^about-university/(?P<pk>\d+)/$', views.AboutUniversityDetailView.as_view(), name='aboutuniversitydetail'),
     #url(r'^calendar/', include('calendarium.urls')),
     url(r'^calendar/', include('happenings.urls', namespace='calendar')),
     #url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
     url(r'^contact/$', views.ContactView.as_view(), name='contact'),
     url(r'^staff_info/$', views.StaffInfoView.as_view(), name='staffinfo'),
     url(r'^faculty_info/$', views.FacultyInfoView.as_view(), name='facultyinfo'),
     url(r'^development_center/$', views.HomeView.as_view(), name='development_center'),
     url(r'^research_center/$', views.HomeView.as_view(), name='research_center'),
     url(r'^publication/$', views.HomeView.as_view(), name='publications'),
     url(r'^placement/$', views.PlacementView.as_view(), name='placement'),
     url(r'^placement/list$', views.PlacementListView.as_view(), name='placementlist'),
     url(r'^placement/complanies$', views.PlacementCompanyView.as_view(), name='placementcompany'),
     
     #url(r'^student$', views.studentView, name='student'),
     #url(r'^student/login$', views.studentLoginView, name='studentlogin'),
     #url(r'^student/logout$', views.studentLogoutView, name='studentlogout'),
     #url(r'^student/auth$', views.studentAuthView, name='studentauth'),
     #url(r'^student/invalid$', views.studentInvalidView, name='studentinvalid'),
     #url(r'^staff$', views.staffView, name='staff'),
     #url(r'^faculty$', views.facultyView, name='faculty'),



)