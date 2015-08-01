from django.shortcuts import redirect ,render
from events.models import *
#from events.forms import TeamInlineFormSet
from django.core.urlresolvers import reverse, reverse_lazy
#from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
#from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin#, DetailView
from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404


#from events.forms import InlineTeamFormSet
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
        path = self.request.META['HTTP_REFERER']
        if "register" in path:
            context['load_after_register'] = 1 #True for jvascript code on eventsdetail.html
        return context

    def get_queryset(self):
        return self.object.event_set.all()

class OCView(SingleObjectMixin, ListView):
    
    template_name = "events/ocdetail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super(OCView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OCView, self).get_context_data(**kwargs)
        context['category'] = self.object
        #ctx['organising_committee_member_list'] = Organising_Committee_Member.objects.all()
        # path = self.request.META['HTTP_REFERER']
        # if "register" in path:
        #     context['load_after_register'] = 1 #True for jvascript code on eventsdetail.html
        return context

    def get_queryset(self):
        return self.object.event_set.all()

class SubEventView(SingleObjectMixin, ListView):
    
    template_name = "events/subevent.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super(SubEventView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SubEventView, self).get_context_data(**kwargs)
        context['category'] = self.object
        #ctx['organising_committee_member_list'] = Organising_Committee_Member.objects.all()
        # path = self.request.META['HTTP_REFERER']
        # if "register" in path:
        #     context['load_after_register'] = 1 #True for jvascript code on eventsdetail.html
        return context

    def get_queryset(self):
        return self.object.event_set.all()

# class TeamRegisterationView(CreateView):
#     model = Team
#     form_class = TeamForm
#     template_name = 'events/registerteam.html'
#     success_url = reverse_lazy('events:teammemberregisteration')

#     # def get_object(self, queryset=None):
#     #     return Shop.objects.get(id = self.kwargs['pk'])

#     def form_valid(self, form):
#         form.instance.event = self.event
#         return super(TeamRegisterationView, self).form_valid(form)
        
#     def dispatch(self, *args, **kwargs):
#         """Ensure the Event exists before creating a new Team."""
#         self.event = get_object_or_404(Event, pk=kwargs['pk'])
#         return super(TeamRegisterationView, self).dispatch(*args, **kwargs)

#     def get_context_data(self, **kwargs):
#         """Add current event to the context, so we can show it on the page."""
#         context = super(TeamRegisterationView, self).get_context_data(**kwargs)
#         context['event'] = self.event
#         return context


class TeamRegisterationView(CreateView):
    template_name = 'events/team1.html'
    model = Team
    form_class = TeamForm # the parent object's form

    #On successful form submission
    def get_success_url(self):
        #return reverse('events:team-created')
        redirect_to = "/events/"+str(self.event.id) + "/"#self.request.GET.get('nextp') #request.GET.get('next','from')
        return redirect_to

    def get_context_data(self, **kwargs):
        context=super(TeamRegisterationView, self).get_context_data(**kwargs)
        context['from']=self.request.GET.get('from',None)
        return context


    def dispatch(self, *args, **kwargs):
        """Ensure the Event exists before creating a new Team."""
        self.event = get_object_or_404(Event, pk=kwargs['pk'])
        self.redirect_to = self.request.GET.get('from')
        return super(TeamRegisterationView, self).dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        
        # Handles GET requests and instantiates blank versions of the form
        # and its inline formsets.
        
        TeamInlineFormSet = inlineformset_factory(Team,
            Team_Member,
            form=TeamMemberForm,
            extra=self.event.team_size,
            can_delete=False,
            can_order=False
        )
        #redirect_to = self.redirect_to #request.GET.get('from',None)
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_member_form = TeamInlineFormSet()
        #instruction_form = InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  #redirect_to=redirect_to,
                                  team_member_form=team_member_form))
                                  #instruction_form=instruction_form

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        TeamInlineFormSet = inlineformset_factory(Team,
            Team_Member,
            form=TeamMemberForm,
            extra=self.event.team_size,
            can_delete=False,
            can_order=False
        )
        #redirect_to = "/events/"+str(self.event.id) + "/"#self.request.GET.get('from')#redirect_to #args[-1]#self.kwargs['from']#
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_member_form = TeamInlineFormSet(self.request.POST)
        if (form.is_valid() and team_member_form.is_valid()):
            return self.form_valid(form, team_member_form)#,redirect_to)
        else:
            return self.form_invalid(form, team_member_form)
    
   

    # Validate forms
    def form_valid(self, form, team_member_form):#,redirect_to):
        form.instance.event = self.event
        #redirect_to = self.redirect_to
        self.object = form.save()
        team_member_form.instance = self.object
        team_member_form.save()
        #redirect_to = self.args[0]
        return HttpResponseRedirect(self.get_success_url())#redirect_to)#)get_success_url()#self.kwargs['from'])#self.get_success_url())

    def form_invalid(self, form, team_member_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  team_member_form=team_member_form))
        
   


# class TeamMemberRegisterationView(CreateView):

#     model = Team_Member
#     form_class = TeamMemberForm
#     template_name = 'events/teammemberregistration.html'
#     success_url = reverse_lazy('events:event')

#     def get_context_data(self, **kwargs):
#         context = super(TeamMemberRegisterationView, self).get_context_data(**kwargs)
#         team_size = self.event.team_size
#         InlineTeamFormSet = inlineformset_factory(Team, Team_Member, form = TeamMemberForm, extra=team_size)
#         if self.request.POST:
#             context['team_member_form'] = InlineTeamFormSet(self.request.POST)
#         else:
#             context['team_member_form'] = InlineTeamFormSet()

#         return context

#     def dispatch(self, *args, **kwargs):
#         """Ensure the Event exists before creating a new Team."""
#         self.event = get_object_or_404(Event, pk=kwargs['pk'])
#         return super(TeamMemberRegisterationView, self).dispatch(*args, **kwargs)

#     def form_valid(self, formset, form):
        
#         context = self.get_context_data()
        
#         team_member_form = context['team_member_formset']
#         team_member_form.instance.team = self.event.team
        
#         if team_member_form.is_valid():
#             self.object = form.save()
#             team_member_form.instance = self.object
#             team_member_form.save()
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form))

#     '''      
# class TeamMemberRegisterationView(BaseInlineFormSet):
#     # When overriding methods on InlineFormSet, you should subclass BaseInlineFormSet rather than BaseModelFormSet.
#    def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop("request")
#         super(TeamMemberRegisterationView, self).__init__(*args, **kwargs)
    
#     def clean(self):
#         super(TeamMemberRegisteration, self).clean()
#         # example custom validation across forms in the formset
#         for form in self.forms:
#             # your custom formset validation
#             ...
# `   '''


# def teamCreatedView(request):
#     # if not request.session.get('form-submitted', False):
#     #     # handle the case where there is no form submitted
#     #     return HttpResponseRedirect(reverse('events:teamregisteration'))
#     # template = loader.get_template('polls/submitted.html')
#     # context = RequestContext(request, request.session.get('registration'))
#     return render(request, 'events/team-created.html')

class OCRegisterationView(CreateView):
    template_name = 'events/ocdetail.html'
    model = Team
    form_class = TeamForm # the parent object's form

    # On successful form submission
    def get_success_url(self):
        #return reverse('events:team-created')
        redirect_to=self.request.GET.get('nextp') #request.GET.get('next','from')
        return redirect_to

    def get_context_data(self, **kwargs):
        context=super(TeamRegisterationView, self).get_context_data(**kwargs)
        context['from']=self.request.GET.get('from',None)
        return context


    def dispatch(self, *args, **kwargs):
        """Ensure the Event exists before creating a new Team."""
        self.event = get_object_or_404(Event, pk=kwargs['pk'])
        self.redirect_to = self.request.GET.get('from')
        return super(TeamRegisterationView, self).dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        TeamInlineFormSet = inlineformset_factory(Team,
            Team_Member,
            form=TeamMemberForm,
            extra=self.event.team_size,
            can_delete=False,
            can_order=False
        )
        redirect_to = self.redirect_to #request.GET.get('from',None)
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_member_form = TeamInlineFormSet()
        #instruction_form = InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  redirect_to=redirect_to,
                                  team_member_form=team_member_form))
                                  #instruction_form=instruction_form

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        TeamInlineFormSet = inlineformset_factory(Team,
            Team_Member,
            form=TeamMemberForm,
            extra=self.event.team_size,
            can_delete=False,
            can_order=False
        )
        redirect_to = "/events/"+str(self.event.id) + "/"#self.request.GET.get('from')#redirect_to #args[-1]#self.kwargs['from']#
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        team_member_form = TeamInlineFormSet(self.request.POST)
        if (form.is_valid() and team_member_form.is_valid()):
            return self.form_valid(form, team_member_form,redirect_to)
        else:
            return self.form_invalid(form, team_member_form)
    
   

    # Validate forms
    def form_valid(self, form, team_member_form,redirect_to):
        form.instance.event = self.event
        #redirect_to = self.redirect_to
        self.object = form.save()
        team_member_form.instance = self.object
        team_member_form.save()
        #redirect_to = self.args[0]
        return HttpResponseRedirect(redirect_to)#self.get_success_url())##)get_success_url()#self.kwargs['from'])#self.get_success_url())

    def form_invalid(self, form, team_member_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  team_member_form=team_member_form))


    