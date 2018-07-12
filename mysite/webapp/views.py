from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>FIFA WORLD CUP 2018</h2>")