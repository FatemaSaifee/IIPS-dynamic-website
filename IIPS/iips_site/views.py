from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def example_bootstrap_toolkit(request):
	return render(request,'example_bootstrap_toolkit.html')