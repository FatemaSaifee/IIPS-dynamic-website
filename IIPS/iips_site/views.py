from django.shortcuts import render
from django.http import HttpResponse
from iips_site.models import *
from django.template import RequestContext,loader
from django.views import generic
from django.utils import timezone


# Create your views here.

#get all model on one template
#option 1
"""
all_models_dict = {
        "template_name": "contacts/index.html",#"iips_site/index.html"
        "queryset": Individual.objects.all(),#News.objects.all(),
        "extra_context" : {"role_list" : Role.objects.all(),#"gallary_list" : Gallary.objects.all(),
                           "venue_list": Venue.objects.all(),# "course_list" :  Course.objects.all(),
                           #and so on for all the desired models...
                           }
    }
"""

#option2

"""
class IndexView(ListView):
context_object_name = 'home_list'    
template_name = 'contacts/index.html'
queryset = Individual.objects.all()

def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['roles'] = Role.objects.all()
    context['venue_list'] = Venue.objects.all()
    context['festival_list'] = Festival.objects.all()
    # And so on for more models
        return context
"""

class IndexView(generic.ListView):
    template_name = 'iips_site/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
    	return News.objects.order_by('-pub_date')[:5]
   	
class GallaryView(generic.ListView):
    template_name = 'iips_site/gallary.html'
    context_object_name = 'latest_photo_list'

    def get_queryset(self):
    	return Gallary.objects.all()[:5]
    	
'''
class ProgramsView(generic.IndexView):
	
	template_name = 'iips_site/programs.html'
	context_object_name = 'programs_list'

	def get_queryset(self):
        return Course.objects.all()

class SyllabusView(generic.IndexView):
	
	template_name = 'iips_site/syllabus.html'
	context_object_name = 'course_list'

	def get_queryset(self):
    	return Course_Content.objects.all()

'''
class Staff_infoView():
	pass


def example_bootstrap_toolkit(request):
	return render(request,'example_bootstrap_toolkit.html')



