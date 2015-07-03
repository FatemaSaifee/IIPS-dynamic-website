from django.shortcuts import render
from events.models import *
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from django.forms.models import inlineformset_factory


# Create your views here.
class EventView(ListView):
    model = Category
    template_name = 'events/event.html'

    def get_context_data(self, **kwargs):
        ctx = super(EventView, self).get_context_data(**kwargs)
        ctx['organising_committee_member_list'] = Organising_Committee_Member.objects.all()
        ctx['event_list'] = Event.objects.all() 
        return ctx

class EventDetailView(SingleObjectMixin, ListView):
    
    template_name = "events/eventdetail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super(EventDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['category'] = self.object
        if self.request.POST:
            context['team_member_form'] = TeamMemberFormSet(self.request.POST)
            context['team_form'] = TeamFormSet(self.request.POST)
        else:
            context['team_member_form'] = TeamMemberFormSet()
            context['team_form'] = TeamFormSet()
        return context
      

    def get_queryset(self):
        return self.object.event_set.all()

    def form_valid(self, form):
        context = self.get_context_data()
        team_member_form = context['team_member_formset']
        team_form = context['team_formset']
        if bookimage_form.is_valid() and bookpage_form.is_valid():
            self.object = form.save()
            team_member_form.instance = self.object #maybe it is .object
            team_member_form.save()
            team_form.instance = self.object
            team_form.save()
            return HttpResponseRedirect('thanks/')
        else:
            return self.render_to_response(self.get_context_data(form=form))

    


def register(request, author_id):
    Team = Team.objects.get(pk=author_id)
    TeamInlineFormSet = inlineformset_factory(Team, Team_Member, fields=('title',))
    if request.method == "POST":
        formset = TeamInlineFormSet(request.POST, request.FILES, instance=team)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(team.get_absolute_url())
    else:
        formset = TeamInlineFormSet(instance=team)
    return render_to_response("events/event.html", {
        "formset": formset,
    })

