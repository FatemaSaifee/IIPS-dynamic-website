from django.conf.urls import patterns, url
from iips_site import views

#get all model on one template
#option1
"""
from django.views.generic import list_detail
urlpatterns = patterns('',
	(r'^$', list_detail.object_list, all_models_dict),
)
"""

#option2

"""
url(r'^$', 
    IndexView.as_view(),
    name="home_list"
        ),
"""
urlpatterns = patterns('',
     url(r'^$', views.IndexView.as_view(), name='index'),
     url(r'^gallary/$', views.GallaryView.as_view(), name='gallary'),
     #url(r'^programs/$', views.ProgramsView.as_view(), name='programs')
)