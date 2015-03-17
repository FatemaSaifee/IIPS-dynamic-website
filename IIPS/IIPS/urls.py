from django.conf.urls import patterns, include, url

from iips_site import views
from data_entry import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IIPS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^example_bootstrap_toolkit',views.example_bootstrap_toolkit),
    #url(r'^$', views.index, name='index'),
    url(r'^iips/', include('iips_site.urls',namespace = 'iips_site')),
    #url(r'^data_entry/', include('data_entry.urls', namespace = 'data_entry')),
    #url(r'^temp_table/$', 'data_entry.views.temp_table',name='home'),
	url(r'^$', 'data_entry.views.login'),   #displays login.html
	#url(r'^accounts/auth/$', 'data_entry.views.auth_view'),    #authorize login
	#url(r'^accounts/loggedin', 'data_entry.loggedin_view'),
	#url(r'^accounts/invalid$', 'data_entry.invalid_view'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
