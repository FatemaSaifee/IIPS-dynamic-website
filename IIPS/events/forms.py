from django.forms.models import inlineformset_factory,modelform_factory,modelformset_factory
from events.models import Team_Member, Team, Event, TeamMemberForm
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import BaseInlineFormSet



#TeamForm = modelformset_factory(Team, exclude = ("event",))
#TeamMemberForm = modelformset_factory(Team_Member)
InlineTeamFormSet = inlineformset_factory(Team, Team_Member, form = TeamMemberForm)#, extra=5)

class TeamMemberRegisterationView(BaseInlineFormSet):
    # When overriding methods on InlineFormSet, you should subclass BaseInlineFormSet rather than BaseModelFormSet.
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(TeamMemberRegisterationView, self).__init__(*args, **kwargs)

    def add_fields(self, form, index):
        # allow the super class to create the fields as usual
        super(TeamMemberRegisterationView, self).add_fields(form, index)
        try:
            instance = self.get_queryset()[kwargs['pk']]
            pk_value = instance.pk
        except IndexError:
            instance=None
            pk_value = hash(form.prefix)


    def is_valid(self):
        result = super(TeamMemberRegisterationView, self).is_valid()

        for form in self.forms:
            if hasattr(form, 'nested'):
                for n in form.nested:
                    # make sure each nested formset is valid as well
                    result = result and n.is_valid()

        return result
        