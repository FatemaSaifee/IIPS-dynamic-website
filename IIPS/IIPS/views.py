from django.shortcuts import render
from django.http import HttpResponse
from iips_site.models import *
#from django.template import RequestContext,loader
#from django.views import generic
from django.utils import timezone

#from django.views.generic.list import ListView
#from django.views.generic.detail import SingleObjectMixin

from django.core.context_processors import csrf
from django.shortcuts import render_to_response

def studentView(request):
    return render(request, 'iips_site/student.html')

def studentLoginView(request):
    c= {}
    c.update(csrf(request))
    return render_to_response('iips_site/student_login.html', c)

def studentAuthView(request):
    username = request.POST.get('username','')
    x  = 9/0
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/student')
    else:
        return HttpResponseRedirect('/student/invalid')

def studentInvalidView(request):
    return render_to_response('iips_site/student_invalid.html')

def studentLogoutView(request):
    auth.logout(request)
    return render_to_response('iips_site/student_logout.html')

def studentView(request):
    return render(request, 'iips_site/student.html')

def staffView(request):
    return render(request, 'iips_site/staff.html')

def facultyView(request):
    return render(request, 'iips_site/faculty.html')