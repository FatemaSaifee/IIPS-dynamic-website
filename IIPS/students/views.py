from django.shortcuts import render
from django.http import HttpResponse
from iips_site.models import *
from django.template import RequestContext,loader
from django.views import generic
from django.utils import timezone

from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin

from django.core.context_processors import csrf
from django.shortcuts import render_to_response

class BulletinView(SingleObjectMixin, ListView):
	pass

class ShelfView(SingleObjectMixin, ListView):
	pass

class ProfileView(SingleObjectMixin, ListView):
	pass

class ClassroomView(SingleObjectMixin, ListView):
	pass
