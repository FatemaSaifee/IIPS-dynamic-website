from django.shortcuts import render
from django.http import HttpResponse
from iips_site.models import *
from django.template import RequestContext,loader
from django.views import generic
from django.utils import timezone

from django.views.generic.list import ListView
# Create your views here.


class IndexView(ListView):
    model = Course
    template_name = 'iips_site/gallery.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['photo_list'] = Gallary.objects.all()
        ctx['news_list'] = News.objects.order_by('-pub_date')[:5]
        ctx['syllabus_list'] = Syllabus.objects.all()
        ctx['admission_list'] = Admission.objects.get(id = 1)
        ctx['fee_structure_list'] = Fee_Structure.objects.all()

        return ctx

class HomeView(ListView):
    model = Course
    template_name = 'iips_site/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['photo_list'] = Gallary.objects.all()
        ctx['news_list'] = News.objects.order_by('-pub_date')[:5]
        ctx['syllabus_list'] = Syllabus.objects.all()
        ctx['admission_list'] = Admission.objects.get(id = 1)
        ctx['fee_structure_list'] = Fee_Structure.objects.all()

        return ctx
'''
class exampleanjeeView(ListView):
    model = Course
    template_name = 'iips_site/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(exampleanjeeView, self).get_context_data(**kwargs)
        ctx['photo_list'] = Gallary.objects.all()
        ctx['news_list'] = News.objects.order_by('-pub_date')[:5]
        ctx['syllabus_list'] = Syllabus.objects.all()
        ctx['admission_list'] = Admission.objects.get(id = 1)
        ctx['fee_structure_list'] = Fee_Structure.objects.all()

        return ctx

'''
class AdmissionView(ListView):
    model = Admission
    template_name = 'iips_site/sidebar.html'

class ProgramView(ListView):
    model = Course
    template_name = 'iips_site/sidebar.html'

class NewsView(ListView):
    model = News
    template_name = 'iips_site/sidebar.html'

class NotificationView(ListView):
    model = Notification
    template_name = 'iips_site/sidebar.html'

class SyllabusView(ListView):
    model = Syllabus
    template_name = 'iips_site/sidebar.html'

class CalendarView(ListView):
    model = Calendar
    template_name = 'iips_site/sidebar.html'

class PlacementView(ListView):
    model = Placement
    template_name = 'iips_site/sidebar.html'

class StaffInfoView(ListView):
    model = Staff_Info
    template_name = 'iips_site/sidebar.html'

class FacultyInfoView(ListView):
    model = Faculty_Info
    template_name = 'iips_site/sidebar.html'   

class ResearchCellView(ListView):
    model = Research_Cell
    template_name = 'iips_site/sidebar.html'

class DevelopementCenterView(ListView):
    model = Developement_Center
    template_name = 'iips_site/sidebar.html'    

class PubliationView(ListView):
    model = Publiation
    template_name = 'iips_site/sidebar.html'   

def contact(request):
    return render(request, 'iips_site/contact.html')
