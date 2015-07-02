from django.shortcuts import render
from events.models import *
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin

# Create your views here.
class EventView(ListView):
    model = Event
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        ctx = super(EventView, self).get_context_data(**kwargs)
        ctx['organising_committee_member_list'] = Organising_Committee_Member.objects.all()
        ctx['category_list'] = Category.objects.all() 
        return ctx

class IndexView(ListView):
    model = Event
    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['organising_committee_member_list'] = Organising_Committee_Member.objects.all()
        ctx['category_list'] = Category.objects.all() 
        return ctx