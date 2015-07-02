from __future__ import unicode_literals

from django.contrib import admin
from events.models import *
# Register your models here.

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 0

class Sub_EventInline(admin.TabularInline):
    model = Sub_Event
    extra = 0

class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('start_date', 'end_date', 'photo', 'more_info',
                       'title', 'description',
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
    inlines = [GalleryInline , Sub_EventInline]
    
admin.site.register(Event, EventAdmin)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Tag)

