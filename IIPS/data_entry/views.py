from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect

from django.forms.models import modelformset_factory

from data_entry.models import *
from data_entry.forms import *

'''
from django.shortcuts import render
from app_name.forms import AllocationPlanForm

def add(request):
    if request.method == 'POST':
        form = AllocatinPlanForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'page.html', {
    'form': AllocationPlanForm()
})
'''

def login(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validat ion rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = LoginForm() # An unbound form

    return render(request, 'data_entry/login.html', {
        'form': form,
    })



def user_temp(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = User_TempForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = User_TempForm() # An unbound form

    return render(request, 'data_entry/user_temp_form.html', {
        'form': User_TempForm(),
    })

def user_temp_post(self, request, roll_number):

    # Get the profile information from form, validate the data and update the profile
    form = User_TempForm(request.POST)

    if form.is_valid():
        account_type = form.cleaned_data['account_type']
        company = form.cleaned_data['company']
        company_size = form.cleaned_data['company_size']
        address = form.cleaned_data['address']
        billing_address = form.cleaned_data['billing_address']

        # Update the client information
        client = Client.objects.filter(user_id=user_id).update(account_type=account_type, company=company,
                                        company_size=company_size, address=address, billing_address=billing_address)        

        # Use the message framework to pass the message profile successfully updated
        #messages.success(request, 'Profile details updated.')
        return HttpResponseRedirect('/')


    else:
        profile_form = ProfileForm()
        return render(request, 'website/profile.html', {'form': profile_form})



'''
@login_required(login_url='/') #if not logged in redirect to /
def temp_table(request):        
    return render(request, 'temp_table.html')

# Create your views here.
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)      

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def invalid_view(request):
	return render(request, 'invalid.html')

def loggedin_view(request):
	return render(request,'temp_table')
'''
'''
def create_a_my_model(request):
        if request.method == 'POST':
            form = MyModelForm(request.POST)
            if form.is_valid():
                my_model = MyModel()
                my_model.field1 = form.cleaned_data.get('form_field1', 'default1')
                my_model.field2 = form.cleaned_data.get('form_field2', 'default2')
                my_model.save()
        else:        
            form = MyModelForm()
        c = { 'form' : form }
        return HttpResponse('templtate.html', c)
'''

#MyModel : field1, field2

