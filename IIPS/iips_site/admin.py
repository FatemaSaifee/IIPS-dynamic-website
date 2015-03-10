from django.contrib import admin
from iips_site.models import *
from django.contrib import admin 
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline 
from example.models import *



# Register your models here .
#class CourseContentInLine(admin.StackedInline):
class CourseContentInLine(NestedTabularInline):
	model = Course_Content
	fk_name = 'Subject'
	extra = 5

class SubjectInline(NestedStackedInline):
    model = Subject
    extra = 1
    fk_name = 'Course'
    inlines = [CourseContentInLine]

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
class SyllabusAdmin(NestedModelAdmin):
	list_display = ('Semester','Course')

	model = Syllabus
	inlines = [SubjectInline]



admin.site.register(Course, CourseAdmin)
admin.site.register(User_Temp)
admin.site.register(Staff_Info)
admin.site.register(Faculty_Info)
admin.site.register(Syllabus,SyllabusAdmin)


#admin.site.register(Course)


