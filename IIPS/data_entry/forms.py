from django import forms

class LoginForm(forms.Form):
    '''name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=3,
                widget=forms.Select(choices=TITLE_CHOICES))
    birth_date = forms.DateField(required=False)'''

    Roll_Number = forms.CharField(max_length=40)
	Password = forms.CharField(max_length=40)

class User_TempForm(forms.Form):
    '''name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())'''

    Temp_Transaction_ID = forms.CharField(max_length=40)
	First_Name= forms.CharField(max_length=20,null =False)
	
	Last_Name =forms.CharField(max_length=25,null =False)
	Father_Name =forms.CharField(max_length=50)
	Mother_Name =forms.CharField(max_length=50)
	Email =forms.CharField(max_length=50)
	Type =forms.CharField(max_length=50)
	DOB= forms.DateField()
	Local_Address =forms.CharField(max_length=200,null=True)
	Permanent_Address =forms.CharField(max_length=200,null=True)
	Mobile_Number =forms.CharField(max_length=15)
	Telephone_Number =forms.CharField(max_length=200,null=True)
	Roll_Number =forms.CharField(max_length=200,null=True)
	Enrollment_Number =forms.CharField(max_length=200,null=True)
