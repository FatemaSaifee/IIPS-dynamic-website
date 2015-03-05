from django.contrib import admin
from iips_site.models import *


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
	##if we want to decide order of fields in the admin form
	#fields = ['course_name','number_of_semester']
	list_display = ('course_name','program_name','number_of_semester')
	
	list_filter = ['number_of_semester']
	search_fields = ['course_name','program_name']

	fieldsets = [
		(None,		{'fields': ['course_name','program_name','number_of_semester']}),
		('About course',{'fields': ['description','objective','learning_outcomes'], 'classes':['collapse']}),
	]

admin.site.register(Course, CourseAdmin)
admin.site.register(User_Temp)
admin.site.register(Staff_Info)
admin.site.register(Faculty_Info)

#admin.site.register(Course)