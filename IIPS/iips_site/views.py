from django.shortcuts import render
from django.http import HttpResponse
from iips_site.models import *
from django.template import RequestContext,loader
from django.views import generic
from django.utils import timezone

from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
# Create your views here.
def tabs(request):
    return render(request, 'iips_site/tabs.html')


class IndexView(ListView):
    model = Program
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
    model = Program
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
class AdmissionView(generic.ListView):
    model = Admission
    template_name = 'iips_site/admission.html'

    def get_queryset(self):
        
        return Admission.objects.all()

class AdmissionDetailView(SingleObjectMixin, ListView):
    
    template_name = "iips_site/admissiondetail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Admission.objects.all())
        return super(AdmissionDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdmissionDetailView, self).get_context_data(**kwargs)
        context['admission'] = self.object
        context['admission_list'] = Admission.objects.all()

        return context

    def get_queryset(self):
        return self.object.admissionblock_set.all()



class ProgramView(ListView):
    model = Program
    template_name = 'iips_site/program.html'

    def get_queryset(self):
        return Program.objects.all()



class ProgramDetailView(SingleObjectMixin, ListView):
    
    template_name = "iips_site/programdetail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Program.objects.all())
        return super(ProgramDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProgramDetailView, self).get_context_data(**kwargs)
        context['program'] = self.object
        context['program_list'] = Program.objects.all()

        return context

    def get_queryset(self):
        return self.object.course_set.all()


class SyllabusView(ListView):
    model = Course
    template_name = 'iips_site/syllabus.html'

    def get_queryset(self):
        return Course.objects.all()

class SyllabusDetailView(generic.DetailView):
    template_name = "iips_site/syllabusdetail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Course.objects.all())
        return super(SyllabusDetailView, self).get(request, *args, **kwargs)
    def get_queryset(self):
        return self.object.syllabus_set.all()

    def get_context_data(self, **kwargs):
        context = super(SyllabusDetailView, self).get_context_data(**kwargs)
        context['course'] = self.object
        context['course_list'] = Course.objects.all()

        return context


    


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



class CalendarView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'

    def get_queryset(self):
        return Calendar.objects.all()


   

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
        return Research_Cell.objects.all()

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


