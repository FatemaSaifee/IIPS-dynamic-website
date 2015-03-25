from django import forms
from django.forms import ModelForm
from data_entry.models import *


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = '__all__'

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()

		if not cleaned_data:
			raise forms.ValidationError("Fields are required.")

		return cleaned_data

class User_TempForm(ModelForm):
	class Meta:
		model = User_Temp
		#fields = ['Temp_Transaction_ID','First_Name','Full_name','Last_Name','Father_Name','Mother_Name','Email','Type','DOB','Local_Address','Permanent_Address','Mobile_Number','Telephone_Number','Roll_Number','Enrollment_Number']
		exclude = ['Full_Name']
		'''
		 widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
'''

	def clean(self):
		cleaned_data = super(User_TempForm, self).clean()
		if not cleaned_data:
			raise forms.ValidationError("Fields are required.")

		return cleaned_data
