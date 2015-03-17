from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect

from django.forms.models import modelformset_factory

from data_entry.models import Login,LoginForm

def login(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = LoginForm() # An unbound form

    return render(request, 'data_entry/login.html', {
        'form': form,
    })

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