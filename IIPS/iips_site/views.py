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





