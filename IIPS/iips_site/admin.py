from django.contrib import admin
from iips_site.models import *
from django.contrib import admin 
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline 
#from example.models import *



# Register your models here 
class NewsAdmin(admin.ModelAdmin):
	list_display = ('Title','pub_date')
	list_filter = ['pub_date']

class Fee_StructureAdmin(admin.ModelAdmin):
	list_display = ('Course_Name','Group','Fees_Excluding_Student_Services_Fee')
	list_filter = ['Course_Name','Group']

class AdmissionDetailInLine(admin.TabularInline):
	model = Admissionblock
	extra = 1

class AdmissionAdmin(admin.ModelAdmin):
	'''
	fieldsets = [
		('Common Enterance Exam-CET',		{'fields': ['CET','List_Of_Criteria_For_Admission','Admission_Process_In_Affiliated_Colleges_If_Department_Is_Monitoring','Student_Profile_Analysis','Admission_To_NRI_PIO','Entrance_Test','Reservation_Policy_Conversion_Of_Seats','Refund_Of_Fee','Other_Important_points','Hostel_Accomodation','Note'],'classes':['collapse']}),
		('Eligiblity',{'fields': ['Minimum_Percentage_For_Admissions_Eligibility_or_Appearing_In_Entrance_Test','Age_Limit','Non_Eligiblity_For_Admission'], 'classes':['collapse']}),
		('How_To_Apply',{'fields' : ['How_To_Apply'], 'classes':['collapse']}),
		('Councling',{'fields' : ['Councling'],'classes':['collapse']}),
		
	]'''
	inlines = [AdmissionDetailInLine]

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

class CourseInLine(admin.StackedInline):
	model = Course
	extra = 1


class ProgramAdmin(admin.ModelAdmin):
	inlines = [CourseInLine]


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
	list_filter = ['Course','Semester']
	search_fields = ['Semester']

	model = Syllabus
	inlines = [SubjectInline]

class PlacementInLine(admin.TabularInline):
    model = Placement
    extra = 4

class Placement_DetailAdmin(admin.ModelAdmin):
	inlines = [PlacementInLine]

class Anti_RaggingAdmin(admin.ModelAdmin):
	list_display = ('Name','Designation','Contact_No')

class ContactAdmin(admin.ModelAdmin):
	list_display = ('Heading','Description')


admin.site.register(Program, ProgramAdmin)
admin.site.register(Syllabus,SyllabusAdmin)
admin.site.register(Admission,AdmissionAdmin)
admin.site.register(Fee_Structure,Fee_StructureAdmin)
admin.site.register(User_Temp)
admin.site.register(Staff_Info)
admin.site.register(Faculty_Info)
admin.site.register(Gallary)
admin.site.register(News,NewsAdmin)
admin.site.register(Placement_Detail,Placement_DetailAdmin)
admin.site.register(Placement_Cell)
admin.site.register(Placement_Company)
admin.site.register(About_IIPS)
admin.site.register(Director)
admin.site.register(Director_Message)
admin.site.register(Anti_Ragging,Anti_RaggingAdmin)
admin.site.register(Vision_Mission_Goal)
admin.site.register(About_University)
admin.site.register(Contact,ContactAdmin)

#admin.site.register(Course)


