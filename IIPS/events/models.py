from django.db import models

# Create your models here.


class Event(models.Model):
	title = models.CharField(_("title"), max_length=255)
	description = models.CharField(max_length=1500)
	more_info = models.CharField(max_length=30)
	start_date = models.DateTimeField(verbose_name=_("start date"))
    end_date = models.DateTimeField(_("end date"))
    all_day = models.BooleanField(_("all day"), default=False)
    repeat = models.CharField(
        _("repeat"), max_length=15, choices=REPEAT_CHOICES, default='NEVER'
    )
    end_repeat = models.DateField(_("end repeat"), null=True, blank=True)
    description = models.TextField(_("description"))
    location = models.ManyToManyField(
        'Location', verbose_name=_('locations'), blank=True
    )
    #objects = EventManager()
    created_by = models.ForeignKey(
        auth_user_model, verbose_name=_("created by"), related_name='events'
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
        self.clean_repeat()
        self.clean_colors()

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

class Gallary(models.Model):
	photo = models.ImageField(upload_to='documents/gallary/')
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

class Team(models.Model):
	event = models.ForeignKey(Event