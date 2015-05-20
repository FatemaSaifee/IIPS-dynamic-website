from django.shortcuts import render
from django.http import HttpResponse
from iips_site.models import *
from django.template import RequestContext,loader
from django.views import generic
from django.utils import timezone

from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin

#from reportlab.pdfgen import canvas

# Create your views here.
def tabs(request):
    return render(request, 'iips_site/tabs.html')


class IndexView(ListView):
    model = Program
    template_name = 'iips_site/gallary.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['photo_list'] = Gallary.objects.all()
        ctx['admission_list'] = Admission.objects.all
        ctx['program_list'] = Program.objects.all()
        
        return ctx

class GallaryView(ListView):
    model = Program
    template_name = 'iips_site/gallary.html'

    def get_context_data(self, **kwargs):
        ctx = super(GallaryView, self).get_context_data(**kwargs)
        ctx['photo_list'] = Gallary.objects.all()
        ctx['admission_list'] = Admission.objects.all
        ctx['program_list'] = Program.objects.all()
        
        return ctx

class HomeView(ListView):
    model = Program
    template_name = 'iips_site/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()
        ctx['news_list'] = News.objects.order_by('-pub_date')[:5]
        ctx['notification_list']= Notification.objects.order_by('-pub_date')[:5]

        
        return ctx
'''
class exampleanjeeView(ListView):
    context_object_name= 'item_list Course'
    template_name = 'iips_site/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(exampleanjeeView, self).get_context_data(**kwargs)
        ctx['admission_list'] = Admission.objects.get(id = 1)

        return ctx

'''
class AdmissionView(generic.ListView):
    model = Admission
    template_name = 'iips_site/admission.html'

   

class AdmissionDetailView(SingleObjectMixin, ListView):
    
    template_name = "iips_site/admissiondetail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Admission.objects.all())
        return super(AdmissionDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AdmissionDetailView, self).get_context_data(**kwargs)
        ctx['admission'] = self.object
        ctx['admission_list'] = Admission.objects.all()
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx

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
        ctx = super(ProgramDetailView, self).get_context_data(**kwargs)
        ctx['admission'] = self.object
        ctx['admission_list'] = Admission.objects.all()
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx
    def get_queryset(self):
        return self.object.course_set.all()

class AboutIIPSView(ListView):
    model = About_IIPS
    template_name = "iips_site/about-iips.html"

    def get_context_data(self, **kwargs):
        ctx = super(AboutIIPSView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()
        ctx['director_list'] = Director.objects.all()

        return ctx

class AboutIIPSAntiraggingView(ListView):
    model = Anti_Ragging
    template_name = "iips_site/anti-ragging.html"

    def get_context_data(self, **kwargs):
        ctx = super(AboutIIPSAntiraggingView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx

class AboutIIPSDirectorView(ListView):
    model = Director_Message
    template_name = "iips_site/director.html"

    def get_context_data(self, **kwargs):
        ctx = super(AboutIIPSDirectorView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx

class AboutIIPSVisionView(ListView):
    model = Vision_Mission_Goal
    template_name = "iips_site/vision.html"

    def get_context_data(self, **kwargs):
        ctx = super(AboutIIPSVisionView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx

class AboutUniversityView(ListView):
    model = About_University
    template_name = "iips_site/about-university.html"

    def get_context_data(self, **kwargs):
        ctx = super(AboutUniversityView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx

class AboutUniversityDetailView(generic.DetailView):
    template_name = "iips_site/aboutuniversitydetail.html"
    model = About_University

    def get_context_data(self, **kwargs):
        ctx = super(AboutUniversityDetailView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()
        ctx['about_university_list'] = About_University.objects.all()

        return ctx
    '''

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Course.objects.all())
        return super(SyllabusDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SyllabusDetailView, self).get_context_data(**kwargs)
        context['course'] = self.object
        context['course_list'] = Course.objects.all()
        

        return context

    def get_queryset(self):
        return self.object.syllabus_set.all()

    '''

class PlacementView(ListView):
    model = Placement_Cell
    template_name = "iips_site/placement.html"

    def get_context_data(self, **kwargs):
        ctx = super(PlacementView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx

    
class PlacementCompanyView(ListView):
    model = Placement_Company
    template_name = "iips_site/placementcompany.html"

    def get_context_data(self, **kwargs):
        ctx = super(PlacementCompanyView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx

class PlacementListView(ListView):
    model = Placement_Detail
    template_name = "iips_site/placementlist.html"

    def get_context_data(self, **kwargs):
        ctx = super(PlacementListView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx

    
# Syllabus..
class SyllabusView(ListView):
    model = Course
    template_name = 'iips_site/syllabus.html'

    def get_queryset(self):
        return Course.objects.all()

class SyllabusDetailView(SingleObjectMixin, ListView):
    
    template_name = "iips_site/syllabusdetail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Course.objects.all())
        return super(SyllabusDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(SyllabusDetailView, self).get_context_data(**kwargs)
        ctx['admission'] = self.object
        ctx['admission_list'] = Admission.objects.all()
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx
    def get_queryset(self):
        return self.object.syllabus_set.all()


class SyllabusSubjectView(SingleObjectMixin, ListView):
    
    template_name = "iips_site/syllabussubject.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Syllabus.objects.all())
        return super(SyllabusSubjectView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(SyllabusSubjectView, self).get_context_data(**kwargs)
        ctx['admission'] = self.object
        ctx['admission_list'] = Admission.objects.all()
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx
    def get_queryset(self):
        return self.object.subject_set.all()

'''
def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

'''
class NewsView(ListView):
    model = News
    template_name = 'iips_site/news.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx


    

class NotificationView(ListView):
    model = Notification
    template_name = 'iips_site/notification.html'

    
    def get_context_data(self, **kwargs):
        ctx = super(NotificationView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx


class CalendarView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/sidebar.html'

    def get_queryset(self):
        return Calendar.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(CalendarView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx
   

class StaffInfoView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/staffinfo.html'   

    def get_queryset(self):
        return StaffInfo.objects.all()

    

    def get_context_data(self, **kwargs):
        ctx = super(StaffInfoView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx

class FacultyInfoView(ListView):
    context_object_name= 'item_list'
    template_name = 'iips_site/facultyinfo.html'   

    def get_queryset(self):
        return Faculty_Info.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(FacultyInfoView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx
'''
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
'''
class ContactView(ListView):
    model = Contact
    template_name = 'iips_site/contact.html' 

    def get_context_data(self, **kwargs):
        ctx = super(ContactView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['admission_list'] = Admission.objects.all()

        return ctx   


