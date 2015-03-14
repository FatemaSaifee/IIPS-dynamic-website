import forms

class MyModelForm(forms.Form):
        form_field1 = forms.CharField(max_length=40, required=True)
        form_field2 = forms.CharField(max_length=60, required=False)