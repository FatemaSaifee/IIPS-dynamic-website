from __future__ import unicode_literals

from django.contrib import admin
from events.models import *
from nested_inline.admin import NestedTabularInline , NestedStackedInline, NestedModelAdmin 
# Register your models here.

class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 0
    
class Sub_EventInline(admin.TabularInline):
    model = Sub_Event
    extra = 0

class TeamMembertInLine(NestedTabularInline):
    model = Team_Member
    #fk_name = 'Team'
    extra = 0

class TeamInline(NestedStackedInline):
    inlines = [TeamMembertInLine]
    model = Team
    extra = 0
    classes = ['collapse']
    
class OrganisingCommitteeMemberInline(admin.TabularInline):
    model = Organising_Committee_Member
    extra = 0

class EventAdmin(NestedModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title','start_date', 'end_date', 'photo', 'team_size', 'more_info',
                        'description',
                       )
        }),

        ('Location', {
            'classes': ('collapse',),
            'fields': ('location',)
        }),
        ('Category', {
            'classes': ('collapse',),
            'fields': ('categories',)
        }),
        ('Tag', {
            'classes': ('collapse',),
            'fields': ('tags',)
        }),
        
        
    )

    list_display = ('title', 'start_date', 'end_date')
    list_filter = ['start_date']
    search_fields = ['title']
    date_hierarchy = 'start_date'
    inlines = [GalleryInline , Sub_EventInline, TeamInline, OrganisingCommitteeMemberInline]
    
admin.site.register(Event, EventAdmin)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Gallery)
admin.site.register(Score)

