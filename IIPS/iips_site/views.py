from django.shortcuts import render
from django.http import HttpResponse
from iips_site.models import *
from django.template import RequestContext,loader
from django.views import generic
from django.utils import timezone

from django.views.generic.list import ListView
# Create your views here.


class IndexView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/gallery.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['course_list'] = Course.objects.all()
        ctx['photo_list'] = Gallary.objects.all()
        ctx['news_list'] = News.objects.order_by('-pub_date')[:5]
        ctx['syllabus_list'] = Syllabus.objects.all()
        ctx['admission_list'] = Admission.objects.get(id = 1)
        ctx['fee_structure_list'] = Fee_Structure.objects.all()

        return ctx

class HomeView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['course_list'] = Course.objects.all()
        ctx['photo_list'] = Gallary.objects.all()
        ctx['news_list'] = News.objects.order_by('-pub_date')[:5]
        ctx['syllabus_list'] = Syllabus.objects.all()
        ctx['admission_list'] = Admission.objects.get(id = 1)
        ctx['fee_structure_list'] = Fee_Structure.objects.all()

        return ctx
'''
class exampleanjeeView(ListView):
    context_object_name= 'item_list Course'
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
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'

    def get_queryset(self):
        return Admission.objects.all()

class ProgramView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'

    def get_queryset(self):
        return Course.objects.all()

class NewsView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'

    def get_queryset(self):
        return News.objects.all()

class NotificationView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'

    def get_queryset(self):
        return Notification.objects.all()

class SyllabusView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'

    def get_queryset(self):
        return Syllabus.objects.all()

class CalendarView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'

    def get_queryset(self):
        return Calendar.objects.all()


    def get_queryset(self):
        return Placement.objects.all

class StaffInfoView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'

    def get_queryset(self):
        return Staff_Info.objects.all()

class FacultyInfoView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'   

    def get_queryset(self):
        return Faculty_Info.objects.all

class ResearchCellView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'

    def get_queryset(self):
        return Research_Cell.objects.all

class DevelopementCenterView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html' 

    def get_queryset(self):   
        return Developement_Center.objects.all()

class PubliationView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'  

    def get_queryset(self): 
        return Publiation.objects.all()

def contact(request):
    return render(request, 'iips_site/contact.html')


