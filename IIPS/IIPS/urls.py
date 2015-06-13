from django.conf.urls import patterns, include, url

from iips_site import views
from data_entry import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from . import views
from django.db.models.loading import cache as model_cache
'''
if not model_cache.loaded:
    model_cache.get_models()
'''    
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IIPS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^calendar/', include('happenings.urls', namespace='calendar')),
    url(r'^student$', views.studentView, name='student'),
    url(r'^student/login$', views.studentLoginView, name='studentlogin'),
    url(r'^student/logout$', views.studentLogoutView, name='studentlogout'),
    url(r'^student/auth$', views.studentAuthView, name='studentauth'),
    url(r'^student/invalid$', views.studentInvalidView, name='studentinvalid'),
    url(r'^staff$', views.staffView, name='staff'),
    url(r'^faculty$', views.facultyView, name='faculty'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('iips_site.urls',namespace = "iips_site")),
    url(r'^data_entry/', include('data_entry.urls', namespace = 'data_entry')),
    #url(r'^temp_table/$', 'data_entry.views.temp_table',name='home'),
	url(r'^$', 'data_entry.views.login'),   #displays login.html
    
    
	#url(r'^accounts/auth/$', 'data_entry.views.auth_view'),    #authorize login
	#url(r'^accounts/loggedin', 'data_entry.loggedin_view'),
	#url(r'^accounts/invalid$', 'data_entry.invalid_view'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
