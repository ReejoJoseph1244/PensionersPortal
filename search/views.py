from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request,'search.html')

def nsap(request):
    return redirect("http://stackoverflow.com/")



