from django.contrib import admin
from data_entry.models import *
from django.contrib import admin 
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline 

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class MyUserAdmin(UserAdmin):
    list_filter = UserAdmin.list_filter + ('groups__name',)

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)


class Generate_Transaction_IDAdmin(admin.ModelAdmin):
	list_display = ('Student_Name','Student_Roll_Number','Temp_Transaction_ID')
	fields = ['Student_Name','Student_Roll_Number']
	search_fields = ['Student_Name']
	search_fields = ['Student_Roll_Number']


admin.site.register(Generate_Transaction_ID, Generate_Transaction_IDAdmin)
admin.site.register(User_Temp)