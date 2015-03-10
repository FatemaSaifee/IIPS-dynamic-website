from django.shortcuts import render
from django.http import HttpResponse
from iips_site.models import News
from django.template import RequestContext,loader
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'iips_site/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return News.objects.order_by('-pub_date')[:5]

'''
class ProgramsView(generic.DetailView):
	model = Course
	template_name = '/programs'

class Staff_infoView():
	pass

'''
def example_bootstrap_toolkit(request):
	return render(request,'example_bootstrap_toolkit.html')