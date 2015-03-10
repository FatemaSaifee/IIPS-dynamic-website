from django.conf.urls import patterns, include, url
from iips_site import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IIPS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^example_bootstrap_toolkit',views.example_bootstrap_toolkit),
    #url(r'^$', views.index, name='index'),
    url(r'^$', include('iips_site.urls',namespace = 'iips_site')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
