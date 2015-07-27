from __future__ import unicode_literals

import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.forms import ModelForm
#from .managers import EventManager
from django.core.exceptions import NON_FIELD_ERRORS
auth_user_model = getattr(settings, "AUTH_USER_MODEL", "auth.User")

# Create your models here.

class Event(models.Model):
    title = models.CharField(_("title"), max_length=255, unique=True)
    start_date = models.DateTimeField(verbose_name=_("start date"))
    end_date = models.DateTimeField(_("end date"))
    photo = models.ImageField(upload_to='documents/event/')
    team_size = models.PositiveSmallIntegerField()
    more_info = models.CharField(max_length=30)
    description = models.TextField(_("description"))
    location = models.ManyToManyField(
        'Location', verbose_name=_('locations'), blank=True
    )
    
    categories = models.ManyToManyField(
        'Category', verbose_name=_('categories'), blank=True
    )
    tags = models.ManyToManyField('Tag', verbose_name=_('tags'), blank=True)

    @property
    def l_start_date(self):
        """Localized start date."""
        return timezone.localtime(self.start_date)

    @property
    def l_end_date(self):
        """Localized end date."""
        return timezone.localtime(self.end_date)

    def is_chunk(self):
        return self.l_start_date.day != self.l_end_date.day

    def starts_same_month_as(self, month):
        return self.l_start_date.month == month

    def ends_same_month_as(self, month):
        return self.l_end_date.month == month

    def starts_same_year_month_as(self, year, month):
        return self.l_start_date.year == year and \
            self.l_start_date.month == month

    def starts_same_month_not_year_as(self, month, year):
        return self.l_start_date.year != year and \
            self.l_start_date.month == month

    def starts_ends_same_month(self):
        return self.l_start_date.month == self.l_end_date.month

    def starts_ends_yr_mo(self, year, month):
        yr = self.l_start_date.year == year or self.l_end_date.year == year
        mo = self.l_start_date.month == month or self.l_end_date.month == month
        return yr and mo

    def start_end_diff(self):
        """Return the difference between start and end dates."""
        s = self.l_start_date
        e = self.l_end_date
        start = datetime.date(s.year, s.month, s.day)
        end = datetime.date(e.year, e.month, e.day)
        diff = start - end
        return abs(diff.days)

    def will_occur(self, now):
        """Returns True if the event will occur again after 'now'."""
        return self.end_repeat is None or self.end_repeat >= now.date() or \
            self.l_start_date >= now or self.l_end_date >= now

    def __str__(self):
        return self.title

    def clean(self):
        self.clean_start_end_dates()
        

    def clean_start_end_dates(self):
        if self.start_date and self.end_date:
            if self.l_start_date > self.l_end_date:
                raise ValidationError(
                    "The event's start date must be before the end date."
                )
            elif (self.l_end_date - self.l_start_date) > datetime.timedelta(7):
                raise ValidationError(
                    "Only events spanning 7 days or less are supported."
                )

    def team_size_list(self):
        return range(1,self.team_size+1)

    def is_active(self): 
        if not self.start_date <= timezone.now() <= self.end_date :
            return True

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')






@python_2_unicode_compatible
class Location(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    address_line_1 = models.CharField(
        _('Address Line 1'), max_length=255, blank=True)
    address_line_2 = models.CharField(
        _('Address Line 2'), max_length=255, blank=True)
    address_line_3 = models.CharField(
        _('Address Line 3'), max_length=255, blank=True)
    state = models.CharField(
        _('State / Province / Region'), max_length=63, blank=True)
    city = models.CharField(
        _('City / Town'), max_length=63, blank=True)
    zipcode = models.CharField(
        _('ZIP / Postal Code'), max_length=31, blank=True)
    country = models.CharField(_('Country'), max_length=127, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(_('title'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name

class Gallery(models.Model):
	photo = models.ImageField(upload_to='documents/event/gallery')
	event = models.ForeignKey('Event')

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.photo.name 

@python_2_unicode_compatible
class Cancellation(models.Model):
    event = models.ForeignKey(
        Event, related_name="cancellations", related_query_name="cancellation"
    )
    reason = models.CharField(_("reason"), max_length=255)
    date = models.DateField(_("date"))

    def __str__(self):
        return self.event.title + ' - ' + str(self.date)

class Organising_Committee_Member(models.Model):
    event = models.ForeignKey('Event', unique=True)
    name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=12)

    def __unicode__(self):  # Python 3: def __str__(self)
        return self.name

class Sub_Event(models.Model):
    event =models.ForeignKey('Event')
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(_("description"))
    start_date = models.DateTimeField(verbose_name=_("start date"))
    end_date = models.DateTimeField(_("end date"))
    tags = models.ManyToManyField('Tag', verbose_name=_('tags'), blank=True)
    team_size = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='documents/event/sub_event',null=True, blank=True)
    location = models.ManyToManyField(
        'Location', verbose_name=_('locations'), blank=True
    )
    winner_score = models.PositiveSmallIntegerField(null=True, blank=True)
    first_runnerup_score = models.PositiveSmallIntegerField(null=True, blank=True)
    second_runnerup_score = models.PositiveSmallIntegerField(null=True, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self)
        return self.name

    def get_score(self, t):
        if Score.objects.get(team = t,sub_event = self):
            return Score.objects.get(team = t,sub_event = self)
        else:
            return 0
        

class Team(models.Model):
    COLORS = [
        ('eeeeee', _('gray')),
        ('ff0000', _('red')),
        ('0000ff', _('blue')),
        ('00ff00', _('green')),
        ('000000', _('black')),
        ('ffffff', _('white')),
    ]

    try:
        COLORS += USER_COLORS
    except Exception:
        pass

	event = models.ForeignKey('Event')
    name = models.CharField(max_length=50, unique=True)
    leader_1 = models.CharField(max_length=50, null=True)
    leader_2 = models.CharField(max_length=50, null=True)
    color = models.CharField(
        max_length=10, choices=COLORS, default='eeeeee', null=True
    )
    slogan = models.CharField(max_length=150, null=True)
    sub_event = models.ManyToManyField(
        'Sub_Event', verbose_name=_('sub_events'), blank=True
    )

    def get_absolute_url(self):
        return reverse('events:event')#, kwargs={'pk': self.pk})

    def __unicode__(self):  # Python 3: def __str__(self)
        return self.name


    def total_score(self): #returns the total score
        for score in self.score_set.all():
            return score.get_score()

    class Meta:
        verbose_name_plural = 'teams'


class Team_Member(models.Model):
    team = models.ForeignKey('Team')
    name = models.CharField(max_length=50, unique=True)
    roll_number = models.CharField(max_length=12)
    college = models.CharField(max_length=50, default='IIPS')
    contact_number = models.CharField(max_length=11, null=True, blank=True)
    email_address = models.CharField(max_length=50, null=True, blank=True)
    # sub_event = models.ManyToManyField(
    #     'Sub_Event', verbose_name=_('sub_events'), blank=True
    # )

    def __unicode__(self):  # Python 3: def __str__(self)
        return self.name

    


class Score(models.Model):
    RANKS = [
        (1, _('First')),
        (2, _('First Runner-up')),
        (3, _('Second Runner-up')),
    ]

    team = models.ForeignKey('Team')
    sub_event = models.ForeignKey('Sub_Event')
    rank = models.PositiveSmallIntegerField(choices=RANKS)
    
    def get_score(self):
        if self.rank== 1:
            return self.sub_event.winner_score
        elif self.rank == 2:
            return self.sub_event.first_runnerup_score
        elif self.rank == 3:
            return self.sub_event.second_runnerup_score
        else:
            return 0

    def __unicode__(self):  # Python 3: def __str__(self)
        return str(self.team) + ' ' + str(self.sub_event)

    class Meta:
        unique_together = ('team', 'sub_event',)



class Winner(models.Model):
    RANKS = [
        (1, _('First')),
        (2, _('First Runner-up')),
        (3, _('Second Runner-up')),
    ]
    team = models.ForeignKey('Team')
    rank = models.PositiveSmallIntegerField(choices=RANKS)

    def __unicode__(self):  # Python 3: def __str__(self)
        return self.team


class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = ['event',]
        #fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
    }
    def get_absolute_url(self):
        return reverse('events:team-detail', kwargs={'pk': self.pk})

class TeamMemberForm(ModelForm):
    class Meta:
        model = Team_Member
        exclude = ['team']
        #fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        labels = {
            'name': _('Team Member'),
        }
        help_texts = {
            'name': _('Write the full name of team member'),
        }
        error_messages = {
            'name': {
                'max_length': _("This team member's name is too long."),
            },
        }
        def clean(self):
            cleaned_data = super(TeamMemberForm, self).clean()
            if not cleaned_data:
                raise forms.ValidationError("Fields are required.")

            return cleaned_data
