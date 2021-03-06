from django.shortcuts import render
from django.http import HttpResponse
from iips_site.models import *
from django.contrib import auth
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

    ##############################

def staffView(request):
    return render(request, 'iips_site/staff.html')

    ###############################

def facultyView(request):
    return render(request, 'iips_site/faculty.html')

    #################################

def studentView(request):
    return render(request, 'iips_site/student.html')

def accountLoginView(request):
    context= {}
    context['photo_list'] = Gallary.objects.all()
    context['admission_list'] = Admission.objects.all()
    context['program_list'] = Program.objects.all()
    context.update(csrf(request))
    return render_to_response('iips_site/account_login.html', context)

def accountAuthView(request):
    username = request.POST.get('username','')
    #group = request.POST.get('group','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    
    if user:
        for group in user.groups.values_list('name',flat=True):
            if group == 'staff':
                return HttpResponseRedirect('/staff')
            elif group == 'student':
                return HttpResponseRedirect('/student')
            elif group == 'faculty':
                return HttpResponseRedirect('/faculty')
            else :
                return HttpResponseRedirect('/account/invalid')
        return HttpResponseRedirect('/account/invalid')
    else :
        return HttpResponseRedirect('/account/invalid')
    # if user.groups.filter(name=group).exists():
    #     auth.login(request, user)
    #     return HttpResponseRedirect('/account')
    # else:
    #     return HttpResponseRedirect('/account/invalid')

    

def accountInvalidView(request):
    return render_to_response('iips_site/account_invalid.html')

def accountLogoutView(request):
    auth.logout(request)
    return render_to_response('iips_site/account_logout.html')


def accountRegisterView(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(Group.objects.get(name='account'))
            return HttpResponseRedirect("/account/register_success")
    else:
        form = UserCreationForm()
    return render(request, "iips_site/account_register.html", {
        'form': form,
    })


def accountRegisterSuccessView(request):
    return render_to_response('iips_site/account_register_success.html')




def search_page(request):
    form = SearchForm()
    if request.method == "POST":
        f = SearchForm(request.POST)
        if f.is_valid():
            Pets = Pet.objects.filter(animal = f.cleaned_data["text"])
            return HttpResponseRedirect("search.html",{"Pets":Pets},{"form":form})
        else:
            return render_to_response("search.html",{"form":form} , context_instance = RequestContext(request))

def search_page(request):
    form = SearchForm()
    if request.method == "POST":
        f = SearchForm(request.POST)
        if f.is_valid():
            Pets = Pet.objects.filter(animal = f.cleaned_data["text"])
            return HttpResponseRedirect("search.html",{"Pets":Pets},{"form":form})



    return render_to_response("search.html",{"form":form} , context_instance = RequestContext(request))