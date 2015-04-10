from django.conf.urls import patterns, include, url

from iips_site import views
from data_entry import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

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

    url(r'^admin/', include(admin.site.urls)),
    url(r'^iips/', include('iips_site.urls',namespace = "iips_site")),
    url(r'^data_entry/', include('data_entry.urls', namespace = 'data_entry')),
    #url(r'^temp_table/$', 'data_entry.views.temp_table',name='home'),
	url(r'^$', 'data_entry.views.login'),   #displays login.html
    
    
	#url(r'^accounts/auth/$', 'data_entry.views.auth_view'),    #authorize login
	#url(r'^accounts/loggedin', 'data_entry.loggedin_view'),
	#url(r'^accounts/invalid$', 'data_entry.invalid_view'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
