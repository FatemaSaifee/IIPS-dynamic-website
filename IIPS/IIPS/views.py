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

  ###########################


def staffView(request):
    return render(request, 'iips_site/staff.html')

def staffLoginView(request):
    c= {}
    c.update(csrf(request))
    return render_to_response('iips_site/staff_login.html', c)

def staffAuthView(request):
    username = request.POST.get('username','')
    
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user.groups.filter(name='staff').exists():
        auth.login(request, user)
        return HttpResponseRedirect('/staff')
    else:
        return HttpResponseRedirect('/staff/invalid')

def staffInvalidView(request):
    return render_to_response('iips_site/staff_invalid.html')

def staffLogoutView(request):
    auth.logout(request)
    return render_to_response('iips_site/staff_logout.html')


def staffRegisterView(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(Group.objects.get(name='staff'))
            return HttpResponseRedirect("/staff/register_success")
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = UserCreationForm()
        #form = UserCreationForm()
    return render(request, "iips_site/staff_register.html", {
        'form': args['form'],
    })
def staffRegisterSuccessView(request):
    return render_to_response('iips_site/staff_register_success.html')
    ################################

def facultyView(request):
    return render(request, 'iips_site/faculty.html')

def facultyLoginView(request):
    c= {}
    c.update(csrf(request))
    return render_to_response('iips_site/faculty_login.html', c)

def facultyAuthView(request):
    username = request.POST.get('username','')
    
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user.groups.filter(name='faculty').exists():
        auth.login(request, user)
        return HttpResponseRedirect('/faculty')
    else:
        return HttpResponseRedirect('/faculty/invalid')

def facultyInvalidView(request):
    return render_to_response('iips_site/faculty_invalid.html')

def facultyLogoutView(request):
    auth.logout(request)
    return render_to_response('iips_site/faculty_logout.html')


def facultyRegisterView(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(Group.objects.get(name='faculty'))
            return HttpResponseRedirect("/faculty/register_success")
    else:
        form = UserCreationForm()
    return render(request, "iips_site/faculty_register.html", {
        'form': form,
    })
def facultyRegisterSuccessView(request):
    return render_to_response('iips_site/faculty_register_success.html')
    ################################


def studentView(request):
    return render(request, 'iips_site/student.html')

def studentLoginView(request):
    c= {}
    c.update(csrf(request))
    return render_to_response('iips_site/student_login.html', c)

def studentAuthView(request):
    username = request.POST.get('username','')
    
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if user.groups.filter(name='student').exists():
        auth.login(request, user)
        return HttpResponseRedirect('/student')
    else:
        return HttpResponseRedirect('/student/invalid')

def studentInvalidView(request):
    return render_to_response('iips_site/student_invalid.html')

def studentLogoutView(request):
    auth.logout(request)
    return render_to_response('iips_site/student_logout.html')


def studentRegisterView(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(Group.objects.get(name='student'))
            return HttpResponseRedirect("/student/register_success")
    else:
        form = UserCreationForm()
    return render(request, "iips_site/student_register.html", {
        'form': form,
    })


def studentRegisterSuccessView(request):
    return render_to_response('iips_site/student_register_success.html')
